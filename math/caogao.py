# -*- coding: utf-8 -*-

def split_num(n):
	#给定一个整数 拆分为位数列表输出
	# 如 123 -> [1,2,3]
	ret = []
	while(n>=10):
		e = n % 10
		n = n//10
		ret.insert(0,e)
	ret.insert(0,n)
	return ret

def rebuild_num(alist):
	# [1,2,3,4,5] -> 12345
	num = 0
	for i in range(len(alist)):
		num = num + alist[i] * pow(10,len(alist)-1-i)
	return num



if __name__ == '__main__':
	import time
	t1 = time.time()
	a = 97679
	alist = split_num(a)
	alist.pop(len(alist)//2)
	b = rebuild_num(alist)
	t2 = time.time()
	print(a,b,t2-t1)


