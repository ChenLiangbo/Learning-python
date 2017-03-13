#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import input_data
from keras.optimizers import SGD

model = Sequential([
	    Dense(100, batch_input_shape=(None, 784)),
		Activation('relu'),
		Dense(10),
		Activation('softmax'),
		])



trainNumber = 5000
testNumber  = 1000
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)
x_train, y_train, x_test, y_test = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
print "x_train.shape = ",x_train.shape
x_train = x_train[0:trainNumber]
y_train = y_train[0:trainNumber]
x_test = x_test[0:testNumber]
y_test = y_test[0:testNumber]
print "x_train.shape = ",x_train.shape
# x_train = x_train.reshape(-1, 28, 28, 1)
# x_test  = x_test.reshape(-1, 28, 28, 1)
'''
print "load data successfully!"
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(
	optimizer=sgd,
	loss='categorical_crossentropy',
	metrics=['accuracy'])

model.fit(x_train, y_train, nb_epoch= 2, batch_size = )
print "train model successfully"

score = model.evaluate(x_test, y_test, batch_size=16)
np.save('score',score)
'''
np.save('y_test',y_test)