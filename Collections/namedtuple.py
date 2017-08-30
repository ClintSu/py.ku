# -*- coding:utf-8 -*- 
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#和class有些类似

from collections import namedtuple

# 定义一个namedtuple类型User，并包含name，sex和age属性。
User= namedtuple('User',['name','sex','age'])

# 创建一个User对象
user=User(name='kong',sex='male',age=21)
print (user)

# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user=User._make(['kong', 'male', 21])
print (user)

# 获取用户的属性
print (user.name)
print (user.sex)
print (user.age)

# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print (user)

# 将User对象转换成字典，注意要使用"_asdict"
print (user._asdict())