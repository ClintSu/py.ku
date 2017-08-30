# -*- coding:utf-8 -*- 

# Counter #计数器--做统计时使用
# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
# 其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）

from collections import Counter
c = Counter() #创建一个空Counter类
c = Counter('gallahad') # 从一个可iterable对象（list、tuple、dict、字符串等）创建
c = Counter({'a':4,'b':2})# 从一个字典对象创建
c = Counter(a=4,b=2)# 从一组键值对创建

#实例
string= 'we are family and we love peace.We have the Greatwall and the yellow river!' 
str_dict={'A':2,'B':5,'G':7,'E':90,'M':6,'N':6, 'x':20,'z':30}   
cou0 = Counter()#创建出来一个空的Counter类  
print (cou0) 

cou1 = Counter(string)#以字符串形式创建Counter类  
print ('cou1 为：------>', cou1)  
cou2 = Counter(str_dict)#以字典形式创建Counter类  
print ('cou2 为：------>', cou2)  
cou3 = Counter(A=1, B=2, x=23, y=34, z=45, o=-5, m=0)#以类字典形式创建即使用键值组合直接创建  
print ('cou3 为：------>', cou3)  	

print ('cou3中所有元素计数总数为：')  
print (sum(cou3.values()))  

print ('将cou3中的键转为列表为：')  
print (list(cou3))  

print ('将cou3中的键转为集合为：')  
print (set(cou3))

print ('将cou3中的键转为列表为：')  
print (dict(cou3))

print ('将cou3中的键值转为(elem, count)形式为：')  
print (cou3.items()) 

print ('取出计数值最小的前4个元素：')  
print (cou2.most_common()[:-5:-1]) 

print ('b 的值为------>', cou1['b'])  
print ('a 的值为------>', cou1['a'])  
cou1.update('balabalabalabalabala')#增加  
print ('b 的值为------>', cou1['b'])  
print ('a 的值为------>', cou1['a'])  

cou2.subtract('AA')#这样导致‘A’的值为0但是并不是删除了key值  
cou2.subtract('MMMMMMMMMM')#这样的话‘M’的值就是负数了  
print ('A 的值为------>', cou2['A'])  
print ('M 的值为------>', cou2['M']) 
print ('cou2 为：------>', cou2)  

#上面A并没有被删除，删除需要使用del方法  
del cou2['A']  
print ('cou2 为：------>', cou2)#这里就没有A的key值了  

#elements()方法  
#返回元素重复次数大于等于1的元素  
print (list(cou3.elements()))  
#一般的运算操作也是满足的  
print ('cou2 和 cou3之和为：')  
print (cou2 + cou3)
print ('cou2 和 cou3之差为：')  
print (cou2 - cou3) 
print ('cou2 和 cou3并集为：')  
print (cou2 | cou3)  
print ('cou2 和 cou3差集为：')  
print (cou2 & cou3)  
 


