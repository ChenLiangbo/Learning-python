import numpy as np
import theano
from theano import tensor as T
from theano import function

x = T.dmatrix('x')
y = T.dmatrix('y')

z = x + y

f = function([x,y],z)
a = np.array([[1,2,3,4],[3,4,5,6]])
b = np.array([[2,2,2,2],[0,9,8,7]])
print "f(x,y) = "
print f(a,b)