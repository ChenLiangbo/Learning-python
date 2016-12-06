#!usr/bin/env/python 
# -*- coding: utf-8 -*-

a = 1
b = 2
c = a + b
print ("a = ",a)

# a = input("input a:")
# print a

s1 = "HuQianshan"

print "s1 = ",s1
print dir(s1)
print "-"*80
print s1.startswith('h')

#list

list1 = [1,2,3,4,5,6]
print "list1 = ",list1
print "-"*80

list1.append(7)
print "list1 = ",list1
print list1.pop(0)
print "list1 = ",list1

print (list1[0],list1[1])
#dict
# adict = {"a":1,"b":2,"c":3}
# print (adict["a"],adict["b"])

# for i in list1:
#     print i
# print "-"*20
# for key in adict:
#     print "key = ",key
#     print "value = ",adict[key]
#     print "----"


# #tuple
# atuple = (1,2,3,4,5,6)


# alist = [list1,s1,atuple]
# print alist

'''
flag = True

if flag:
    print "flag = True"
elif flag == True:
    print "elif"
else:
    print "else"
'''

i = 7
j = 8
# "i = 7,j = 8"
print "i = %d,j = %d" % (i,j)

l = range(0,19)
print l 

squared = [x ** 2 for x in range(4)]
print squared