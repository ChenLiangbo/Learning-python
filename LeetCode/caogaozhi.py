#!usr/bin/env/python 
# -*- coding: utf-8 -*-
import time 

def f1(n):
    results = 1
    for i in range(n):
        results = results*(i+1)
    return results


def f2(n): 
    if n == 1:
        return n
    else:
        return n*f2(n-1)

if __name__ == '__main__':
    t0 = time.time()
    n = 300
    n1 = f1(n)
    t1 = time.time()
    print("n1 = ",n1,"t = ",t1 - t0)
    n2 = f2(n)
    t2 = time.time()
    print("n2 = ",n2,"t = ",t2 - t1)