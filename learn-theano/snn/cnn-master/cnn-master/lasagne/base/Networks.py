#!/usr/bin/env python

from __future__ import print_function

import sys
import os

import numpy as np
import theano
import theano.tensor as T
import lasagne

# for the larger networks (blocks_length>=9), we need to adjust pythons recursion limit
sys.setrecursionlimit(10000)

# ##################### Build the neural network model #######################

from lasagne.layers import Conv2DLayer as ConvLayer
#from lasagne.layers.dnn import Conv2DDNNLayer as ConvLayer
from lasagne.layers import ElemwiseSumLayer
from lasagne.layers import InputLayer
from lasagne.layers import DenseLayer
from lasagne.layers import GlobalPoolLayer
from lasagne.layers import PadLayer
from lasagne.layers import ExpressionLayer
from lasagne.layers import NonlinearityLayer
from lasagne.nonlinearities import linear, rectify
from lasagne.layers import batch_norm

def buildResNet(input_var, inshape=(105,111), n_predictions=3, blocks_length=3, filter_count=16):
    # create a residual learning building block with two stacked 3x3 convlayers as in paper
    def residual_block(l, increase_dim=False, projection=False):
        input_num_filters = l.output_shape[1]
        if increase_dim:
            first_stride = (2,2)
            out_num_filters = input_num_filters*2
        else:
            first_stride = (1,1)
            out_num_filters = input_num_filters

        stack_1 = batch_norm(ConvLayer(l, num_filters=out_num_filters, filter_size=(3,3), stride=first_stride, nonlinearity=rectify, pad='same', W=lasagne.init.HeNormal(gain='relu'), flip_filters=False))
        stack_2 = batch_norm(ConvLayer(stack_1, num_filters=out_num_filters, filter_size=(3,3), stride=(1,1), nonlinearity=None, pad='same', W=lasagne.init.HeNormal(gain='relu'), flip_filters=False))

        # add shortcut connections
        if increase_dim:
            if projection:
                # projection shortcut, as option B in paper
                projection = batch_norm(ConvLayer(l, num_filters=out_num_filters, filter_size=(1,1), stride=(2,2), nonlinearity=None, pad='same', b=None, flip_filters=False))
                block = NonlinearityLayer(ElemwiseSumLayer([stack_2, projection]),nonlinearity=rectify)
            else:
                # identity shortcut, as option A in paper
                if l.output_shape[2] % 2 == 1:
                    trailWidth = 1
                else:
                    trailWidth = 0

                if l.output_shape[3] % 2 == 1:
                    trailHeight = 1
                else:
                    trailHeight = 0

                identity = ExpressionLayer(l, lambda X: X[:, :, ::2, ::2], lambda s: (s[0], s[1], s[2]//2+trailWidth, s[3]//2 + trailHeight))
                padding = PadLayer(identity, [out_num_filters//4,0,0], batch_ndim=1)
                block = NonlinearityLayer(ElemwiseSumLayer([stack_2, padding]),nonlinearity=rectify)
        else:
            block = NonlinearityLayer(ElemwiseSumLayer([stack_2, l]),nonlinearity=rectify)
        
        return block

    # Building the network
    l_in = InputLayer(shape=(None, 1, inshape[0], inshape[1]), input_var=input_var)

    # first layer, output is 64 x 32 x 32
    l = batch_norm(ConvLayer(l_in, num_filters=filter_count, filter_size=(7,7), stride=(1,1), nonlinearity=rectify, pad='same', W=lasagne.init.HeNormal(gain='relu'), flip_filters=False))
        
    # first stack of residual blocks, output is 64 x 32 x 32
    for _ in range(blocks_length):
        l = residual_block(l)

    # second stack of residual blocks, output is 128 x 16 x 16
    l = residual_block(l, increase_dim=True)
    for _ in range(1,blocks_length):
        l = residual_block(l)

    # third stack of residual blocks, output is 256 x 8 x 8
    l = residual_block(l, increase_dim=True)
    for _ in range(1,2*blocks_length):
        l = residual_block(l)

    # third stack of residual blocks, output is 512 x 8 x 8
    l = residual_block(l, increase_dim=True)
    for _ in range(1,blocks_length):
        l = residual_block(l)

    # average pooling
    l = GlobalPoolLayer(l)

    # fully connected layer
    network = DenseLayer(
            l, num_units=n_predictions,
            W=lasagne.init.HeNormal(),
            nonlinearity=linear)# ScaledTanH(scale_in=1, scale_out=25))

    print("number of parameters in model: %d" % lasagne.layers.count_params(network, trainable=True))

    return network