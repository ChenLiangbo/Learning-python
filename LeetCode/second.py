#!usr/bin/env/python 
# -*- coding: utf-8 -*-

class Solution(object):
    
    def isSameList(self,list1,list2):
        list1.sort()
        list2.sort()
        return (list1 == list2)
    def inMatix(self,alist,matrix):
        for m in matrix:
        	if self.isSameList(alist,m):
        	    return True
        return False
    
    # 返回序列中所有的和为0的三个数
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        length = len(nums)
        for i in range(length-2):
            for j in range(i+1,length-1):
            	for k in range(j+1,length):
            		target = nums[i] + nums[j] + nums[k]
            		if target == 0:
            		    ret.append([nums[i],nums[j],nums[k]])
        
        if len(ret) < 2:
            return ret

        results = [ret[0],]
        for list1 in ret[1:]:
            if not self.inMatix(list1,results):
            	results.append(list1)
        return results
    
    #在序列中找到和最接近给定值的解
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = 3
        ret = []
        cloeset = 2**32
        length = len(nums)
        if length == 3:
            return sum(nums)

        for i in range(length-2):
            for j in range(i+1,length-1):
            	for k in range(j+1,length):
            		asum = nums[i] + nums[j] + nums[k]
            		if asum > target:
            		    diff = asum - target
            		else:
            			diff = target - asum
            		if diff < cloeset:
            		    cloeset = diff
            		    ret = asum
        return ret
    # 十进制整数转换为罗马数字字符串
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i = 0
        ret = ''
        while(num != 0):
            if num >= base[i]:
                num -= base[i]
                ret += roman[i]
            else:
                i = i + 1
        return ret
    # 罗马数字字符串转换为十进制整数
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tag = {"I":1,"V":5,"X":10,"C":100,"M":1000,"L":50,"D":500}
        val = 0
        for i in range(len(s)):
            if (i+1>=len(s)) or (tag[s[i+1]] <= tag[s[i]]):
                val = val + tag[s[i]]
            else:
                val -= tag[s[i]]

        return val

    #去除列表中所有与给定元素相同的元素
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while(val in nums):
            index = nums.index(val)
            if index == 0:
                nums = nums[1:]
            elif index+1 == len(nums):
                nums = nums[:index]
            else:
                nums = nums[:index].extend(nums[index+1:])
            # nums.pop(index)
        return len(nums)

    def helpCombine(self,zero,one):
        ret = []
        for i in zero:
            for j in one:
                ret.append(i+j)
        return ret

    # LeetCode 17 :给出一串数字字符串，将其对应的所有手机键盘的英文组合给出，返回字符串列表
    def letterCombinations(self, digits):
        """
        :type digits: str '123'
        :rtype: List[str]
        """
        principle = {'1':['',],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                    '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                    '':[],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if len(digits) <= 1:
            return principle[digits]
        length = len(digits)
        ret = principle[digits[0]]
        for i in range(1,length):
            ret = self.helpCombine(ret,principle[digits[i]])
        return ret

    #LeetCode 21,合并列表，新列表只是将量列表的节点相连
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if len(l1) == 0:
            l1 = []
        list(l1).extend(l2)
        return l1
    
    #LeetCode 29 不使用乘法 除法和模运算符号实现整数的除法
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # ret = 

    # LeetCode 23,Merge k sorted linked lists and return it as one sorted list.
    # Analyze and describe its complexity
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return []
        if len(lists) == 1:
            return lists[0]

        ret = list([])
        for alist in lists:
            ret.extends(alist)
        ret.sort()
        return ret
        


if __name__ == '__main__':
    import time
    t1 = time.time()
    solution = Solution()
    # nums = [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]
    # print("solution = ",solution.threeSum(nums))
    # nums = [89,-17,-41,9,56,-8,40,38,98,-31,80,-1,-40,-73,28,55,15,89,-83,87,-42,-22,61,64,-94,-33,-38,25,-20,-80,37,99,-72,74,16,-25,-21,-73,-73,-72,65,-4,-72,46,60,7,-25,-14,-58,-50,14,-99,88,50,75,-59,94,-74,25,23,-10,-47,-1,-30,81,-66,54,-64,-1,68,-1,47,55,-59,5,64,45,83,-3,-38,-59,46,33,54,55,9,-13,50,-43,-48,57,97,-55,-13,-25,-9,-20,63,30,88,-4,74,19,-87,-32]
    # print("solution = ",solution.divide(-3,-1))
    # print("running time = ",time.time() - t1)
    sample = [[],[]]
    solution.mergeKLists(sample)