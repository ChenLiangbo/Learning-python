#!usr/bin/env/python 
# -*- coding: utf-8 

#!usr/bin/env/python 
# -*- coding: utf-8 
import random

str1 = list(input("input number string1:"))
str2 = list(input("input number string2:"))

def snwap(aString):
	length = len(aString)
	index1 = int(length*random.random()//1)
	index2 = int(length*random.random()//1)
	if index1==index2:
		index1 = index1 -1
	if index1 < 0:
		index1 = index1 + 2
	aString[index1],aString[index2] = aString[index2],aString[index1]
	return aString

str1_1 = ''.join(snwap(str1))
str2_1 = ''.join(snwap(str2))
print("str1_1 = ",str1_1)
print("str2_1 = ",str2_1)