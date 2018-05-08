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

    def moFangMatrix(self,n):
        '''
        Func : 给定一个整数数n，生成一个魔方矩阵
        In   : n ,int
        Out  : matix
        '''
        import numpy as np
        if n%2 != 0:
            elements = list(range(1,n*n+1))
            print(elements)
            matrix   = np.zeros((n,n),dtype = np.int16)

            sx = 0        # 初始行序号 
            sy = (n+1)//2 -1  # 初始列序号

            matrix[sx,sy] = elements[0]

            for i in range(1,len(elements)):
       
                x = sx
                y = sy

                sx = sx - 1
                sy = sy + 1

                if sx < 0 and sy <= n-1:
                    sx = n - 1

                if sx >= 0 and sy > n-1:
                    sy = 0

                if sx < 0 and sy > n-1:
                    sy = y
                    sx = sx + 1

                if int(matrix[sx,sy]) != 0:
                    sy = y
                    sx = sx + 1


                print((sx,sy),elements[i])
                

                matrix[sx,sy] = elements[i]
                


            return matrix

        else:
            if n%4 == 0:
                pass
            else:
                pass
    def merge2Lists(self,list1,list2):
        '''
        Func: merge two sorted lists
        In  : list(list1,list2)
        Out : list
        '''
        result = []
        if type(list1) == 'NoneType':
            return list2
        if type(list2) == 'NoneType':
            return list1
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] < list2[0]:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
        result = result + list1
        result = result + list2
        return result


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) <= 1:
            try:
                return lists[0]
            except:
                return None
        elif len(lists) == 2:
            return self.merge2Lists(lists[0],lists[1])
        else:
            index = len(lists)//2
            left  = lists[0:index]
            right = lists[index:]
            return self.merge2Lists(self.mergeKLists(left),self.mergeKLists(right))
            

if __name__ == '__main__':
    solution = LessonTime()
    l1 = [1,3,5,7,9]
    l2 = [0,2,4,6,8,10,12]
    l3 = [1,2,3,4,6,8,13,15,34,45,67]
    l4 = [2,4,6,8,9,12,14,13,15,19,23,24]
    l5 = []

    lists = list([[],l1,l2,l3,l4,l5])
    print("lists = ",lists)
    result = solution.mergeKLists(lists)
    print("result = ",result)
