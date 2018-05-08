#!usr/bin/env/python 
# -*- coding: utf-8 -*-

# 第一种
# 无序列表中的查找，随机查找，循环遍历


#第二种 有序表的查找一般使用二分法
#不断从中间选取元素进行查找，这样的时间复杂度是log(n)
#在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False
 
# 分查找法虽然已经很不错了，但还有可以优化的地方。
# 有的时候，对半过滤还不够狠，要是每次都排除十分之九的数据岂不是更好？选择这个值就是关键问题，插值的意义就是：以更快的速度进行缩减。

# 插值的核心就是使用公式：
# value = (key - list[low])/(list[high] - list[low])

# 用这个value来代替二分查找中的1/2。