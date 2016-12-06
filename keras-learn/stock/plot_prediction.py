import numpy as np
from matplotlib import pyplot as plt

y_predict = np.load('y_predict.npy')
y_test    = np.load('y_test.npy')

y_predict = y_predict[0:100]
y_test = y_test[0:100]

plt.plot(y_test,'ro')
plt.plot(y_predict,'bo')
plt.plot(y_test,'r-')
plt.plot(y_predict,'b-')
plt.legend(['y_test','y_predict'])
plt.grid(True)
plt.xlabel('index')
plt.ylabel('value')
plt.title('Keras BPNN Predict Close With AllOneDay')
plt.savefig('close.jpg')
plt.show()
