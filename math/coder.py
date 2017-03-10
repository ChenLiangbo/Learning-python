# -*- coding: utf-8 -*-

sentence = 'I love You'

# for i in sentence:
#     print("i = %s,ascii = %d" % (i,ord(i)))

# print(chr(64))

import datetime

bo = '1992-10-10'
pp = '1994-03-13'
f = '%Y-%m-%d'
bt = datetime.datetime.strptime(bo,f)
pt = datetime.datetime.strptime(pp,f)
print("bt = ",type(bt))
dt = bt - pt
print("days = ",dt.days)