# -*- coding:utf-8 -*- 

import sys
import configparser
config = configparser.ConfigParser()

'''
config.read("config.conf")
print(sys.path[0])
'''
config.read(sys.path[0] + "/config.conf")

#返回所有的section
s=config.sections()
print ('section:',s)

#获取指定section的options
o=config.options('db')
print ('options:',o)

#获取指定section的配置信息
v=config.items('db')
print ('db:',v)

#获取指定option
db_host=config.get('db','db_host')
print (db_host)

#获取整形
thread = config.getint("concurrent", "thread") 
print (thread) 

#-------、
#添加(修改)option值
config.set('db','db_pass','zkzk')
config.write(open("config.conf","w"))

#添加一个section
config.add_section('kkkk')
config.set('kkkk','int','15')
config.set('kkkk','bool','true')
config.write(open("config.conf","w"))

#移除
#config.remove_option('kkkk','int')
config.remove_section('kkkk')
config.write(open("config.conf","w"))
