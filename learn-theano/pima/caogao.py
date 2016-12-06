#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import numpy as np
import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer

print "strart ..."

dataset = np.load('pima-indians.npy')

columns = np.hsplit(dataset,9)
xsample = np.hstack(columns[0:8])
ysample = columns[8]
shape = xsample.shape
print "xsample = ",xsample.shape
print "ysample = ",ysample.shape

# indexList = np.random.permutation(shape[0])
indexList = range(shape[0])

x_train = xsample[indexList[0:538]]
y_train = ysample[indexList[0:538]]
print "x_train.shape = ",x_train.shape
print "y_train.shape = ",y_train.shape

x_test = xsample[indexList[538:]]
y_test = ysample[indexList[538:]]
print "x_test.shape = ",x_test.shape
print "y_test.shape = ",y_test.shape

training_data, validation_data, test_data = network3.data_shared(x_train,y_train,x_test,y_test)
mini_batch_size = 40
iter_times = 60
learn_rate = 0.01

net = Network([
               FullyConnectedLayer(n_in = 8, n_out = 15),
               SoftmaxLayer(n_in = 15, n_out = 2)], mini_batch_size)
print "net okay"
net.SGD(training_data, iter_times, mini_batch_size, learn_rate,
        validation_data, test_data)
print "train okay"