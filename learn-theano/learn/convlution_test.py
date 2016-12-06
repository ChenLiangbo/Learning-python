#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import numpy
import theano
from theano import tensor as T
from theano.tensor.nnet import conv
rng = numpy.random.RandomState(23455)
# print "rng.shape = ",type(rng)
# print dir(rng)
input = T.tensor4(name='input')

w_shp = (2, 3, 9, 9)
w_bound = numpy.sqrt(3 * 9 * 9)
W = theano.shared( numpy.asarray(
	rng.uniform(
		low=-1.0 / w_bound,
		high=1.0 / w_bound,
		size=w_shp),
	dtype = input.dtype), name ='W')

b_shp = (2,)
b = theano.shared(numpy.asarray(
	rng.uniform(low=-.5, high=.5, size=b_shp),
	dtype=input.dtype),
	name ='b')

conv_out = conv.conv2d(input, W)

output = T.nnet.sigmoid(conv_out + b.dimshuffle('x', 0, 'x', 'x'))

f1 = theano.function([input], output)
maxpool_shape = (2, 2)
pool_out = downsample.max_pool_2d(input, maxpool_shape, ignore_border=True)
f2 = theano.function([input],pool_out)
print "It is okay"