#!usr/bin/env/python 
# -*- coding: utf-8 -*-

# LeetCode 
import math
class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

    def median(self,alist,blist):
        alist.extend(blist)
        alist.sort()
        print("alist = ",alist)
        length = len(alist)
        if length % 2 != 0:
            ret = alist[int(length/2)]
        else:
            ret = alist[int(length/2)] + alist[int(length/2) - 1]
            ret = ret/2
        return ret

    #在字符串中找到最长且没有重复字符的子字符串
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subList = []
        sub = []
        for i in range(len(s)):
            if s[i] not in sub:
                sub.append(s[i])
            else:
                subList.append(sub)
                index = sub.index(s[i])
                sub = sub[index+1:]
                sub.append(s[i])
        subList.append(sub)
        length = 0 
        for s in subList:
            if len(s) > length:
                length = len(s)
        return length

    #判断是否为回文字符串
    def isPalindrome(self,s):
        length = len(s)
        for i in range(int(length/2)):
            if s[i] != s[length-1-i]:
                return False
        return True

    # 寻找字符中最长的非重复子字符串
    def longestPalindrome(self, s):
        """
        :type s: str  
        :rtype: str
        """
        palinList = []
        palin = []
        for i in s:
            if i not in palin:
                palin.append(i)
            else:
            	index = palin.index(i)
            	new = palin[index:]
            	new.append(i)
            	if self.isPalindrome(new):
            	    palin.append(i)
            	else:
            	    palinList.append(palin)
            	    palin = []
        palinList.append(new)
        print("palinList = ",palinList)
        length = 0
        for palin in palinList:
        	if len(palin) > length:
        	    length = len(palin)
        return length
                
    #将一个整数颠倒
    def reverse(self, x):
        """
        :type x: int 将一个整数颠倒
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
        x = abs(x)
        x = list(str(x))
        if isNegative:
            x.append('-')
        x.reverse()
        x = ''.join(x)
        return int(x)

    # 判断是否为回文数
    def isPalindromeNumber(self, x):
        """
        :type x: int 
        :rtype: bool
        """
        if x < 0:
            x = str(x)[1:]
        else:
            x = str(x)
        length = len(x)
        for i in range(int(length/2)):
            if x[i] != x[length-1-i]:
                return False
        return True
    
    # n x n 将以个矩阵顺时针旋转九十度
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]  
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        dst = []
        for i in range(n):
            row = matrix[i]
            dst.extend(row)
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = dst[i*n+j]
        return matrix
    
    # 判断两个排序后的列表是不是所有元素都相同
    def isSameList(self,nums1,nums2):
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True

    #辅助全排列的函数
    def helpPermutations(self,num,numsList):
        ret = []
        for i in range(len(numsList)):
            nums = [num,]
            anum = numsList[i].copy()
            nums.extend(anum)
            ret.append(nums)
        return ret

    # 列表元素的全排列
    def permutations(self,nums):
        """
        :type nums: List[int] 
        :rtype: List[List[int]]
        """
        if len(nums) <=1:
            return nums
        elif len(nums) == 2:
            return [nums,[nums[1],nums[0]]]
        else:
            ret = []
            for i in range(len(nums)):
                anum = nums.copy()
                e = anum.pop(i)
                enum = self.permutations(anum)
                ret.extend(self.helpPermutations(e,enum))
            return ret

    def isSameList(self,nums1,nums2):
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True

    # 判断一个列表是不是在由列表所组成的矩阵中
    def listInMatrix(self,alist,matrix):
        if len(matrix) == 0:
            return False
        for m in matrix:
            if self.isSameList(alist,m):
                return True
        return False
    
    #将矩阵中排序后相同的列表去除
    def unique(self,numsList):
        length = len(numsList)
        ret = []
        for nums in numsList:
            if not self.listInMatrix(nums,ret):
                ret.append(nums)
        return ret
    # # 列表组合
    def permuteUnique(self, nums):
        """
        :type nums: List[int]     
        :rtype: List[List[int]]
        """
        return self.unique(self.permutations(nums))

    def listValue(self,alist):
        asum = 0
        for i in range(len(alist)):
            asum = asum + alist[i]*10**i
        return asum

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num = self.listValue(l1) + self.listValue(l2)
        print(self.listValue(l1),self.listValue(l2))
        num = str(num)
        ret = list(num)
        ret.reverse()
        for i in range(len(ret)):
            ret[i] = int(ret[i])
        return ret

    # 列表中四个数的和是给定的值，返回所有的组合 
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        ret = []
        for i in range(length-3):
            for j in range(i+1,length-2):
                for k in range(j+1,length-1):
                    for m in range(k+1,length):
                        aslice = [nums[i],nums[j],nums[k],nums[m]]
                        if sum(aslice) == target:
                            ret.append(aslice)
        return ret 

    #LeetCode 20 : 判断一个字符串是不是合法的输入 2.8%
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = ['()','[]','{}']
        count = 0
        for c in valid:
            if c in s:
                count = count + 1
                cindex = s.index(c)
                start = cindex
                end = start + 2
                s = s[:start] + s[end:]
                print("c = ",c,"cindex = ",cindex,"s = ",s)
                if len(s) == 2:
                    if s in valid:
                        return True
                    else:
                        return False
                if len(s) == 0:
                    return True
        if count < 1:
            return False
        else:
            return self.isValid(s)

    # LeetCode 20 : 4.58%
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v1 = '[]'
        v2 = '()'
        v3 = '{}'
        v = [v1,v2,v3]
        flag = False
        if v1 in s:
            cindex = s.index(v1)
            start = cindex
            end = start + 2
            s = s[:start] + s[end:]
            flag = True

        if v2 in s:
            cindex = s.index(v2)
            start = cindex
            end = start + 2
            s = s[:start] + s[end:]
            flag = True

        if v3 in s:
            cindex = s.index(v3)
            start = cindex
            end = start + 2
            s = s[:start] + s[end:]
            flag = True
        
        if not flag:
            return flag

        if len(s) == 0:
            return True
        elif len(s) == 2:
            if s in v:
                return True
            else:
                return False
        elif len(s) == 1:
            return False
        else:
            return self.isValid2(s)

    # LeetCode 22: 给定个数，产生合法的括号字符串
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        c1 = '('
        c2 = ')'
        c = [c1,c2]
        ret = []
        
# s = 'abccbajjklss'
solution = Solution()

s = solution.isValid2("()")
print("s = ",s)
