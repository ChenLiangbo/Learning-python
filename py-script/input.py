#!usr/bin/env/python 
# -*- coding: utf-8 -*-

# raw_input : You can input anything but get only string
# input : You can only input python object and get python object,int,str,float,

def pop_achar(aList,achar):
    # Pop a kind of character from a list,no matter how many characters in list
    if achar in aList:
        index = aList.index(achar)
        aList.pop(index)
        pop_achar(aList,achar)
    return aList


def input_a_list():
    # Input a list from terminate
    # Change number from string to float if with number
    aString = raw_input("raw_input a vector,endwith enter:")
    aList = aString.split(' ')
    aList = pop_achar(aList,'')
    for i in range(len(aList)):
        try:
            aList[i] = float(aList[i])
        except Exception as ex:
            print("[Exception Information]",str(ex))
            aList[i] = aList[i]
    return aList

if __name__ == '__main__':
    aList = input_a_list()  # Input anything,get str or float in list



