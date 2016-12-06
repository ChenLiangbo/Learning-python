# -*- coding: utf-8 -*-
import numpy as np
m = 10
n = 10
B = [1.0/m]*m
B = np.array(B).reshape(len(B),1)
print "B = ",B
print "B.shape = ",B.shape
print "-"*80
A = np.random.randn(m,n)
A = np.int32(3*np.fabs(A))
print A
print "A.shape = ",A.shape

iterTimes = 10
legend = ['Bn_1','Bn']
Bn = B
from matplotlib import pyplot as plt
dberror = 2
i = 0
while(dberror > 0.00000001):
    Bn_1 = Bn
    Bn = A*Bn
    Bn = Bn/np.sum(Bn)
    db = Bn[:,0] - Bn_1[:,0]
    db = db/np.sum(db)
    # bn = Bn[:,0].tolist()
    # bn_1 = Bn_1[:,0].tolist()
    # plt.plot(bn_1,'ro')
    # plt.plot(bn,'bo')
    # plt.legend(legend)
    # plt.plot(bn_1,'r-')
    # plt.plot(bn,'b-')
    # plt.show()
    # tf.reduce_mean(tf.square((Y - y_out)))
    
    e1 = dberror
    dberror = db.var()
    print "i = %d, e1 = %f,error = %f" % (i,e1,dberror)
  
    if i > 1000:
        break
    i = i + 1
    # break

bn = Bn_1[:,0].tolist()
bn_1 = Bn[:,0].tolist()
plt.plot(bn_1,'ro')
plt.plot(bn,'bo')
plt.legend(legend)
plt.plot(bn_1,'r-')
plt.plot(bn,'b-')
plt.show()


