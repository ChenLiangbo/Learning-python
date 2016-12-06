#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
training_data, validation_data, test_data = network3.load_data_shared()
print "start net"

mini_batch_size = 128

net = Network([
	ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28),
		filter_shape=(20, 1, 5, 5),
		poolsize=(2, 2)),
	FullyConnectedLayer(n_in=20*12*12, n_out=100),
	SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)

print "training net"
net.SGD(training_data, 60, mini_batch_size, 0.1,
	validation_data, test_data)