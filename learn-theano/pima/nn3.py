#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import theano
import theano.tensor as T
from theano import function
from theano.ifelse import ifelse
import numpy as np
from random import random

# http://www.cnblogs.com/love6tao/p/5773160.html
inputNumber = 8
layerOne    = 15
ouputNumber = 1

learnRate   = 0.01


