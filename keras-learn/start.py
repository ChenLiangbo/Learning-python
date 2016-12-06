#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from keras.layers.core import Dense, Dropout, Flatten, Activation,Flatten
from keras.models import Sequential,Model
from keras.optimizers import Adam

# for a single-input model with 2 classes (binary):
model = Sequential()
model.add(Dense(1, input_dim=784, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# generate dummy data
import numpy as np
data = np.random.random((1000, 784))
labels = np.random.randint(2, size=(1000, 1))

# train the model, iterating on the data in batches
# of 32 samples
model.fit(data, labels, nb_epoch=10, batch_size=32)