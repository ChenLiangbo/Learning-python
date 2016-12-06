import numpy as np
import theano
from theano import tensor as T
from theano import function

print "start ..."

x = T.dscalar('x')
y = T.dscalar('y')

z = x + y
print "ppz = ",theano.pp(z)
f = function([x,y],z)
a = np.array([[1,2,3,4],[3,4,5,6]])
b = np.array([[2,2,2,2],[0,9,8,7]])
print "f(2,5) = ",f(2,5)
# print f(a,b)
print z.eval({x:16.3,y:7.7})