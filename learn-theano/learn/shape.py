#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import theano
import theano.tensor as T
from theano import function
import numpy as np

x = theano.tensor.matrix('x')
x_specify_shape = theano.tensor.specify_shape(x, (2, 2))
f = theano.function([x], (x_specify_shape ** 2).shape)
theano.printing.debugprint(f) 