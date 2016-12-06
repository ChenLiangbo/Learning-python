#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import theano
import theano.tensor as T
from theano import function
from theano.ifelse import ifelse
import numpy as np
from random import random

# http://www.cnblogs.com/love6tao/p/5773160.html

x= T.vector();
W= T.matrix();
z = T.dot(W,x)
#y = 1.0/(1.0+np.exp(-z))
y = np.exp(z)/T.sum(np.exp(z), axis=0) # 0  是按列 1 是按行
log_activation = theano.function(inputs=[W,x],outputs=y)

x = np.array([1 ,1.4 ,1.5],dtype=theano.config.floatX)
W = np.array([[1.1,1.2,1.3],[0.1,0.2,0.4],[0.2,0.5,2.1]],dtype=theano.config.floatX)

for i in range(x.shape[0]):
   print 'i =  %d ,out = %.2f ' %( i+1, log_activation(W,x)[i])

c=log_activation(W,x)
y_class = np.argmax(c,axis=0)
print y_class+1