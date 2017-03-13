#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import numpy as np


from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

x = range(1,11)
y = [3,5,2,8,4,6,4,12,7,9]
plt.bar(x,y, alpha = .4, color = 'r')
plt.grid(True)
plt.show()
