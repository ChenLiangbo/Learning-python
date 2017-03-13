#!usr/bin/env/python 
# -*- coding: utf-8 -*-

import Queue

q = Queue.Queue()   # FIFO

print("="*80)
for i in range(5):
    q.put(i)
print('-'*40)
while not q.empty():
    print q.get()

print("="*80)


q = Queue.LifoQueue() # LIFO

for i in range(5):
    q.put(i)
print('-'*40)
while not q.empty():
    print q.get()
print("="*80)

# Queue.Empty
# Queue.Full
# q.get(block=True, timeout=None)
# q.get_nowait()
# q.put(item, block=True, timeout=None)
# q.put_nowait(item)