#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import theano  
import theano.tensor as T  
import numpy as np  
import network3

training_data, validation_data, test_data = network3.load_mnist()  
x_train,t_train = training_data[0],training_data[1]
x_test, t_test  = test_data[0],test_data[1]

number = x_train.shape[0]
print "number = ",number
'''
# 加载数据  
x_train, t_train, x_test, t_test = load_cifar.cifar10(dtype=theano.config.floatX)  
labels_test = np.argmax(t_test, axis=1)  
'''

# 定义标识性Theano变量  
x = T.matrix()  
t = T.matrix()  
  
# 定义模型：神经网络  
def floatX(x):  
    return np.asarray(x, dtype=theano.config.floatX)  
  
def init_weights(shape):  
    return theano.shared(floatX(np.random.randn(*shape) * 0.1))  
  
def momentum(cost, params, learning_rate, momentum):  
    grads = theano.grad(cost, params)  
    updates = []  
      
    for p, g in zip(params, grads):  
        mparam_i = theano.shared(np.zeros(p.get_value().shape, dtype=theano.config.floatX))  
        v = momentum * mparam_i - learning_rate * g  
        updates.append((mparam_i, v))  
        updates.append((p, p + v))  
  
    return updates  
  
def model(x, w_h1, b_h1, w_h2, b_h2, w_o, b_o):  
    h1 = T.maximum(0, T.dot(x, w_h1) + b_h1)  
    h2 = T.maximum(0, T.dot(h1, w_h2) + b_h2)  
    p_y_given_x = T.nnet.softmax(T.dot(h2, w_o) + b_o)  
    return p_y_given_x  
  
w_h1 = init_weights((28 * 28, 100))  
b_h1 = init_weights((100,))  
w_h2 = init_weights((100, 100))  
b_h2 = init_weights((100,))  
w_o = init_weights((100, 10))  
b_o = init_weights((10,))  
  
params = [w_h1, b_h1, w_h2, b_h2, w_o, b_o]  
  
p_y_given_x = model(x, *params)  
y = T.argmax(p_y_given_x, axis=1)  
  
cost = T.mean(T.nnet.categorical_crossentropy(p_y_given_x, t))  
  
updates = momentum(cost, params, learning_rate=0.001, momentum=0.9)  
  
  
# 编译theano函数  
train = theano.function([x, t], cost, updates=updates)  
predict = theano.function([x], y)  
  
# train model  
batch_size = 50  
  
for i in range(50):  
    for start in range(0, number, batch_size):  
        x_batch = x_train[start:start + batch_size]  
        t_batch = t_train[start:start + batch_size]  
        cost = train(x_batch, t_batch)  
  
    predictions_test = predict(x_test)  
    accuracy = np.mean(predictions_test == labels_test)  
    print "iteration %d - accuracy: %.5f" % (i + 1, accuracy) 