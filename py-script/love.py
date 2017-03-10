#!python
#coding:utf-8

# print（'\n'.join([''.join([('LoveYaer '[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)]) for y in range(15,-15,-1)])，）


# print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))*2 else' 'for x in range(-80,20)])for y in range(-20,20)])


# for i in range(0,20):
    # print ("i={0}".format(i))
    # print ("i = ",i)

# print("some text,", end="")


def xrange():
	pass

# assert(xrange == range)
l = [i for i in range(20)]
print ("l = ",type(l),dir(l))

d = {"a":1,"b":2,"c":3}
print ("d = ",type(d),dir(d),)
keys = list(d.keys())
print ("keys = ",keys,type(keys))