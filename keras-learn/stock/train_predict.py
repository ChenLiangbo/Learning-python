#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import numpy as np
import os


order ={"0":"Open","1":"High","2":"Low","3":"Close","4":"Volume*e-6"}
yahooData = np.load('yahoo_finance5.npy')
Open,High,Low,Close,Volume = np.hsplit(yahooData,5)

shape = yahooData.shape
x_sample = yahooData[0:shape[0]-1,:]
# x_sample = np.hstack([Open,High,Low,Volume])
# x_sample = x_sample[0:shape[0]-1,:]
y_sample = Close[1:]

xmax = np.amax(x_sample, axis=0)
xmin = np.amin(x_sample, axis=0)
x_sample = (x_sample - xmin) / (xmax - xmin)
ymax = np.amax(y_sample, axis=0)
ymin = np.amin(y_sample, axis=0)
y_sample = (y_sample - ymin) / (ymax - ymin)
print "x_sample.shape = ",x_sample.shape
print "y_sample.shape = ",y_sample.shape

trainNumber = 1000
x_train = x_sample[0:trainNumber]
y_train = y_sample[0:trainNumber]
x_test  = x_sample[trainNumber:]
y_test  = y_sample[trainNumber:]

from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import SGD

inputs = Input(shape=(5,))

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(15, activation='relu')(inputs)
predictions = Dense(1, activation='relu')(x)


# this creates a model that includes
# the Input layer and three Dense layers
model = Model(input=inputs, output=predictions)
model.compile(optimizer='rmsprop',
              loss='mean_squared_error',
              metrics=['accuracy'])
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.11, nesterov=True)

print "training model ..."

model.fit(x_train,y_train,nb_epoch = 10000,batch_size = 12,shuffle=True,verbose = 2)
print "predict ..."
y_predict = model.predict(x_test)
np.save("y_predict",y_predict)
np.save("y_test",y_test)
print "dir = ",dir(model)

# model.save('myModel.hd5')
print "save moddel"

from keras.models import model_from_json  
json_string = model.to_json()  
open('model_architecture.json','w').write(json_string)  
model.save_weights('model_weights.h5')  
 #读取model  
print "load model"
model = model_from_json(open('model_architecture.json').read())  
model.load_weights('model_weights.h5')  

y_predict = model.predict(x_test)

