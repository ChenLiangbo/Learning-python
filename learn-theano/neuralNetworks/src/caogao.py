#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer

print "strart ..."
training_data, validation_data, test_data = network3.load_data_shared()

print "training_data = ",(type(training_data),len(training_data))
x0 = training_data[0]
print "x0 = ",type(x0)

mini_batch_size = 10

net = Network([
               FullyConnectedLayer(n_in=784, n_out=100),
               SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
print "net okay"
net.SGD(training_data, 60, mini_batch_size, 0.1,
        validation_data, test_data)
print "train okay"