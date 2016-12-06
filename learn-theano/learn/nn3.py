#!usr/bin/env/python 
# -*- coding: utf-8 -*-

'''
# import cPickle
# import gzip
filename="./data/mnist.pkl.gz"
f = gzip.open(filename, 'rb')
training_data, validation_data, test_data = cPickle.load(f)
f.close()

trainNumber = 5000
testNumber  = 1000

x_train,y_train = training_data[0][0:trainNumber],training_data[1][0:trainNumber]
x_validation,y_validation = validation_data[0][0:trainNumber],validation_data[1][0:trainNumber]
x_test,y_test = test_data[0][0:testNumber],test_data[1][0:testNumber]
print "x_train.shape = ",(x_train.shape,y_train.shape)
'''
import input_data
trainNumber = 5000
testNumber  = 2000
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)
x_train, y_train, x_test, y_test = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
print "x_train.shape = ",(x_train.shape,y_train.shape)
x_train = x_train[0:trainNumber]
y_train = y_train[0:trainNumber]
x_test = x_test[0:testNumber]
y_test = y_test[0:testNumber]
print "x_train.shape = ",(x_train.shape,y_train.shape)

from theano import tensor as T
from theano import function,shared
import numpy as np

x = T.dmatrix('x')
y = T.dmatrix('y')
