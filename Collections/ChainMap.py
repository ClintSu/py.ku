# -*- coding:utf-8 -*- 
# ChainMap是python3的新特性，它用来将多个map组成一个新的单元（原来的map结构仍然存在，类似于这些map被存在了一个list之中），
# 这比新建一个map再将其他map用update加进来快得多。通过ChainMap可以来模拟嵌套的情景，而且多用于模板之中。

from collections import ChainMap

m1 = {'color': 'red', 'user': 'guest'}
m2 = {'name': 'drfish', 'age': '18'}
chainMap = ChainMap(m1, m2)
print(chainMap.items())

# 获取ChainMap中的元素
print(chainMap.get('name'))
print(chainMap.get('user'))

# 新增map --前面添加
m3 = {'data': '1-6'}
chainMap = chainMap.new_child(m3)
print(chainMap.items())

# parents属性 -- 去除前面
print(chainMap.parents)
print(chainMap.parents.parents)
print(chainMap.parents.parents.parents)

# maps属性
print(chainMap.maps)