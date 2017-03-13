#!usr/bin/env/python 
# -*- coding: utf-8 -*-

import multiprocessing
import numpy as np
import time


pool = multiprocessing.Pool(processes=4)
maxTimes = 100000
t0 = time.time()
for i in range(maxTimes):
    # re = np.exp(i)
    pool.apply_async(np.exp, (i))
pool.close()
pool.join()
print("It took %f seconds" % (time.time() - t0))

# pool = multiprocessing.Pool(processes=4)