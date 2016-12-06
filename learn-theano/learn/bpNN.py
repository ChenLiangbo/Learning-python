#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import numpy as np
import theano
from theano import tensor as T

# http://www.tuicool.com/articles/M7FRziR
'''
np.random.seed(0)  
x_train, y_train = datasets.make_moons(300, noise=0.20)  
x_train = x_train.astype(np.float32)  
y_train = y_train.astype(np.int32)  
num_example = x_train.shape[0]

'''
dataset = np.load('../pima/pima-indians.npy')

columns = np.hsplit(dataset,9)
xsample = np.hstack(columns[0:8])
ysample = columns[8]
ysample = dataset[:,8]
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

num_example = x_train.shape[0]
#设置参数  
nn_input_dim  = 8 #输入神经元个数  
nn_output_dim = 1 #输出神经元个数  
nn_hdim = 15 
#梯度下降参数  
epsilon = 0.01 #learning rate  
reg_lambda = 0.01 #正则化长度  

w1 = theano.shared(np.random.randn(nn_input_dim,nn_hdim),name="W1")  
b1 = theano.shared(np.zeros(nn_hdim),name="b1")  
w2 = theano.shared(np.random.randn(nn_hdim,nn_output_dim),name="W2")  
b2 = theano.shared(np.zeros(nn_output_dim),name="b2")  

#前馈算法  
X = T.dmatrix('X')  #double类型的矩阵  
y = T.lvector('y') #int64类型的向量  
z1 = X.dot(w1)+b1   #1  
a1 = T.tanh(z1)     #2  
z2 = a1.dot(w2)+b2  #3  
y_hat=T.nnet.softmax(z2) #4  
#正则化项  
loss_reg=1./num_example * reg_lambda/2 * (T.sum(T.square(w1))+T.sum(T.square(w2))) #5  
loss = T.nnet.categorical_crossentropy(y_hat,y).mean()+loss_reg  #6  
#预测结果  
prediction     = T.argmax(y_hat,axis=1) #7  
forword_prop   = theano.function([X],y_hat)  
calculate_loss = theano.function([X,y],loss)  
predict        = theano.function([X],prediction)  

#求导  
dw2 = T.grad(loss,w2)  
db2 = T.grad(loss,b2)  
dw1 = T.grad(loss,w1)  
db1 = T.grad(loss,b1)  
  
#更新值  
gradient_step=theano.function(  
    [X,y],  
    updates=(  
        (w2,w2-epsilon*dw2),  
        (b2,b2-epsilon*db2),  
        (w1,w1-epsilon*dw1),  
        (b1,b1-epsilon*db1)  
  
    )  
)  

def build_model(num_passes=20000,print_loss=False):  
  
    w1.set_value(np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim))  
    b1.set_value(np.zeros(nn_hdim))  
    w2.set_value(np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim))  
    b2.set_value(np.zeros(nn_output_dim))  
  
    for i in xrange(0,num_passes):  
        gradient_step(x_train,y_train) 
        break 
        if print_loss and i%100==0:  
            print "Loss after iteration %i: %f" %(i,calculate_loss(x_train,y_train)) 
            break

if __name__ == '__main__':
    build_model()