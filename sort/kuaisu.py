#!usr/bin/env/python 
# -*- coding: utf-8 -*-

def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low

def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v

if __name__ == '__main__':
    s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    print("before sort:",s)
    s1 = quicksort(s, left = 0, right = len(s) - 1)
    print("after sort:",s1)