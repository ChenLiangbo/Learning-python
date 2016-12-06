import numpy as np
import theano
from theano import tensor as T
from theano import function


a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff**2
f = theano.function([a, b], [diff, abs_diff, diff_squared])

out = f([[1, 1], [1, 1]], [[0, 1], [2, 3]])
print "type = ",type(out)
print out