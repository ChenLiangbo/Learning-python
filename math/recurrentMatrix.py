# -*- coding: utf-8 -*-
import numpy as np

def get_matrix_n(n):
	# 生成如下所示的矩阵
	# [[ 1.  2.  3.  4.]
	#  [12. 13. 14.  5.]
	#  [11. 16. 15.  6.]
	#  [10.  9.  8.  7.]]

	def get_new_index(flag,row,col):
		if flag == 'R+':
			row = row + 1
			col = col
		if flag == 'R-':
			row = row -1
			col = col
		if flag == 'C+':
			row = row
			col = col + 1
		if flag == 'C-':
			row = row
			col = col -1
		return row,col

	matrix = np.zeros((n,n))
	FLAGS = ['R+','C+','R-','C-']
	row = 0
	col = 0
	flag = 'C+'
	
	for i in range(1,n*n+1):
		matrix[row,col] = i

		if flag == 'C+':
			if col+1 == n:
				flag = 'R+'
			elif matrix[row,col+1] != 0:
				flag = 'R+'
		if flag == 'R+':
			if row +1 == n:
				flag = 'C-'
			elif matrix[row+1,col] != 0:
				flag = 'C-'
		if flag == 'C-':
			if col == 0:
				flag = 'R-'
			elif matrix[row,col-1] != 0:
				flag = 'R-'
		if flag == 'R-':
			if row == 1:
				flag = 'C+'
			elif matrix[row-1,col] != 0:
				flag = 'C+'

		row,col = get_new_index(flag,row,col)
	return matrix

def solution():
	# 一个九位数a,去除中间的数得到b a能整除b,求有多少个a
	count = 0
	for a1 in range(0,10):
		for a2 in range(0,10):
			for a3 in range(0,10):
				for a4 in range(0,10):
					for a5 in range(0,10):
						for a6 in range(0,10):
							for a7 in range(0,10):
								for a8 in range(0,10):
									for a9 in range(1,10):
										a = a1 + \
										a2 * pow(10,1) + \
										a3 * pow(10,2) + \
										a4 * pow(10,3) + \
										a5 * pow(10,4) + \
										a6 * pow(10,5) + \
										a7 * pow(10,6) + \
										a8 * pow(10,7) + \
										a9 * pow(10,8)

										b = a1 + \
										a2 * pow(10,1) + \
										a3 * pow(10,2) + \
										a4 * pow(10,3) + \
										a6 * pow(10,4) + \
										a7 * pow(10,5) + \
										a8 * pow(10,6) + \
										a9 * pow(10,7)

										if a/b - a//b == 0:
											count = count +1
	return count


def solution2(n = 3):
	count = 0
	la = []
	lb = []
	for a1 in range(0,10):
		for a2 in range(0,10):
			for a3 in range(1,10):
				a = a3*100 + a2*10 + a1
				b = a3*10 + a1
				if a//b - a/b == 0:
					count += 1
					la.append(a)
					lb.append(b)
	return count,la,lb

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

def solution3():
	count = 0
	start = 100000000
	end   = 1000000000
	for i in range(start,end):
		a = i
		alist = split_num(i)
		alist.pop(len(alist)//2)
		b = rebuild_num(alist)
		
		if a//b - a/b == 0:
			count = count + 1
			print(a,b)
	return count



if __name__ == '__main__':
	import time
	# m = get_matrix_n(10)
	# # print(m)
	# diag = np.diag(m)
	# print(np.sum(diag))
	t1 = time.time()

	n = solution3()
	t2 = time.time()
	print("n = ",n.t2-t1)

