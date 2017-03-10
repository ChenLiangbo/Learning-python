# -*- coding: utf-8 -*-
filename = 'test1.txt'

fp = open(filename,'rb')
lines = fp.readlines()
symbol = [b'<',b'>']
outfp = open('result2.txt','ab')
for line in lines:
    # print("line = ",line,type(line))
    # print(dir(line))
    # line = line.encode('utf-8')
    index1 = line.find(symbol[1])
    line = line[index1:]
    # print("index1 = ",index1,line)
    index2 = line.rfind(symbol[0])
    line = line[:index2]
    # print("index2 = ",index2,line)
    index3 = line.find(symbol[1])
    line = line[index3+1:]
    print("index3 = ",index3,line,len(line))
    if len(line) < 2:   #如果不需要序号就注释掉这两句得到result2
        continue
    outfp.write(line)
    outfp.write(b'\r\n')
   
outfp.close()
fp.close()