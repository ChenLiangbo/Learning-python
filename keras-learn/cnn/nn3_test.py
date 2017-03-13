import numpy as np

y_test = np.load('./nn3file/y_test.npy')
score  = np.load('./nn3file/score.npy')

print "y_test.shape = ",y_test.shape
print "score.shape = ",score.shape
print y_test[0:10]
print "-"*80
print score[0:10]