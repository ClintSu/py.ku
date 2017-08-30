# -*- coding:utf-8 -*- 
# deque #双向队列, 算法复杂度O(1)

import collections
d = collections.deque()
d.append(1)
d.append(2) #添加
print(d)

d.appendleft(3) #左侧添加
print(d)
d.extend([7,8,9]) #右侧扩展一个列表
print(d)

d.insert(3,11) #指定位置插入
print(d)

print (d.index(8))
print (d.index(3,0,4)) #指定0~4区间查找

d.pop() #右侧删除
print(d)
d.popleft() #左侧删除
print(d)

d.remove(11) #删除指定
print(d)

d.reverse() #队列反转
print(d)

#把元素放到左侧
dq = collections.deque()
dq.extend(['a','b','c','d','e'])
dq.rotate(2)   #指定次数，默认1次
print(dq)




"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画

import sys
import time
from collections import deque
fancy_loading = deque('>--------------------')
while True:
    print ('\r%s' % ''.join(fancy_loading),fancy_loading.rotate(1))
    sys.stdout.flush()
    time.sleep(0.08)
# Result:
# 一个无尽循环的跑马灯
"""