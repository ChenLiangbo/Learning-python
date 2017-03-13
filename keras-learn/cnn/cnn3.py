#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from __future__ import print_function  
import numpy as np
from keras.models import Sequential  
from keras.layers.core import Dense, Dropout, Activation, Flatten  
from keras.layers.convolutional import Convolution2D, MaxPooling2D  
from keras.optimizers import SGD  
from keras.utils import np_utils  

# There are 40 different classes  
nb_classes = 40  
nb_epoch = 40  
batch_size = 40  
  
# input image dimensions  
img_rows, img_cols = 57, 47  
# number of convolutional filters to use  
nb_filters1, nb_filters2 = 5, 10  
# size of pooling area for max pooling  
nb_pool = 2  
# convolution kernel size  
nb_conv = 3  
def Net_model(lr=0.005,decay=1e-6,momentum=0.9):  
    model = Sequential()  
    model.add(Convolution2D(nb_filters1, nb_conv, nb_conv,  
                            border_mode='valid',  
                            input_shape=(1, img_rows, img_cols)))  
    model.add(Activation('ReLU'))  
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))  
  
    model.add(Convolution2D(nb_filters2, nb_conv, nb_conv))  
    model.add(Activation('tanh'))  
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))  
    #model.add(Dropout(0.25))  
  
    model.add(Flatten())  
    model.add(Dense(1000)) #Full connection  
    model.add(Activation('tanh'))  
    #model.add(Dropout(0.5))  
    model.add(Dense(nb_classes))  
    model.add(Activation('softmax'))  
  
    sgd = SGD(lr=lr, decay=decay, momentum=momentum, nesterov=True)  
    model.compile(loss='categorical_crossentropy', optimizer=sgd)  
      
    return model  
