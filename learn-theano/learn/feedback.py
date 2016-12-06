#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import theano
import theano.tensor as T
from theano.ifelse import ifelse
import numpy as np

# 定义变量:
x = T.vector('x')
w = T.vector('w')
b = T.scalar('b')

# 定义数学表达式:
z = T.dot(x,w)+b
a = ifelse(T.lt(z,0),0,1)

neuron = theano.function([x,w,b],a)


# 定语输入与权重
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
weights = [ 1, 1]
bias = -1.5

# 遍历所有输入并输出结果:
for i in range(len(inputs)):
    t = inputs[i]
    out = neuron(t,weights,bias)
    print 'The output for x1=%d | x2=%d is %d' % (t[0],t[1],out)


print "-"*80

# 定义变量:
x = T.vector('x')
w = theano.shared(np.array([1,1]))
b = theano.shared(-1.5)

# 定义数学表达式:
z = T.dot(x,w)+b
a = ifelse(T.lt(z,0),0,1)

neuron = theano.function([x],a)

# 定义输入和权重
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# 遍历所有输入并得到输出:
for i in range(len(inputs)):
    t = inputs[i]
    out = neuron(t)
    print 'The output for x1=%d | x2=%d is %d' % (t[0],t[1],out)

print "-"*80

# 梯度
import theano
import theano.tensor as T
from theano import function
from theano.ifelse import ifelse
import numpy as np
from random import random

# 定义变量:
x = T.matrix('x')
w = theano.shared(np.array([random(),random()]))
b = theano.shared(1.)
learning_rate = 0.01

# 定义数学表达式:
z = T.dot(x,w)+b
a = 1/(1+T.exp(-z))

a_hat = T.vector('a_hat') #Actual output
cost = -(a_hat*T.log(a) + (1-a_hat)*T.log(1-a)).sum()   #交叉熵损失函数

dw,db = T.grad(cost,[w,b]) #对权重和偏置求导数

train = function(
    inputs = [x,a_hat],
    outputs = [a,cost],
    updates = [
        [w, w-learning_rate*dw],
        [b, b-learning_rate*db]
    ]
)

# 定义输入和权重
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
outputs = [0,0,0,1]

# 遍历所有输入并计算输出:
cost = []
for iteration in range(30000):
    pred, cost_iter = train(inputs, outputs)
    cost.append(cost_iter)

# 打印输出:
print 'The outputs of the NN are:'
for i in range(len(inputs)):
    print 'The output for x1=%d | x2=%d is %.2f' % (inputs[i][0],inputs[i][1],pred[i])

# 绘制损失图:
print '\nThe flow of cost during model run is as following:'
import matplotlib.pyplot as plt

plt.plot(cost)
plt.show()