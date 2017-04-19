#!usr/bin/env/python 
# -*- coding: utf-8 -*-

class LessonTime(object):
    def __init__(self,):
        super(LessonTime,self).__init__()
        self.nums = list(range(1,11))

    #给定一个数num，在0-10之间返回两个数a,b或者三个数a,b,c使得和为,且a,b,c相连
    def getTime(self,num,k):
        result = []
        ret = []
        # 首先尝试两个连续数之和是否满足
        length = len(self.nums)
        for n in range(1,length):
            for i in range(length - n):
                snum = 0
                ret = []
                for j in range(n+1):
                    # print("j = ",j)
                    snum = snum + self.nums[i+j]
                    ret.append(self.nums[i+j])
                if snum == num:
                    result.append(ret)
        for ret in result:
            if len(ret) == k:
                return ret
        return None

    def sumClosestThree(self,nums,target):
        ret = []
        # 首先尝试两个连续数之和是否满足
        length = len(nums)
        n = 3
        for i in range(length - n):
            snum = 0
            ret = []
            for j in range(n+1):
                # print("j = ",j)
                snum = snum + nums[i+j]
                ret.append(nums[i+j])
            if snum == target:
                result.append(ret)

        return ret

solution = LessonTime()
print("solution = ",solution.getTime([-1,2,1,-4],1))
