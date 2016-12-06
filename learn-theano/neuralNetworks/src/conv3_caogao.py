#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import network3
from network3 import ReLU
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer



training_data, validation_data, test_data = network3.load_data_shared()
print "training_data.shape = ",training_data.shape
print "validation_data.shape = ",validation_data.shape
print "test_data.shape = ",test_data.shape
net = Network([
	ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28),
		filter_shape=(20, 1, 5, 5),
		poolsize=(2, 2)),
	ConvPoolLayer(image_shape=(mini_batch_size, 20, 12, 12),
		filter_shape=(40, 20, 5, 5),
		poolsize=(2, 2),
		activation_fn=ReLU),
	FullyConnectedLayer(n_in=40*4*4, n_out=100, activation_fn=ReLU),
	SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)

print "training ..."
net.SGD(training_data, 60, mini_batch_size, 0.1,
	validation_data, test_data,lmbda=0.1)