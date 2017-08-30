# -*- coding:utf-8 -*- 

class Kls(object):
    def __init__(self, data):
        self.data = data
    def printd(self):
        print(self.data)
    @staticmethod
    def smethod(*arg):
        print('Static:', arg)
    @classmethod
    def cmethod(*arg):
        print('Class:', arg)

ik = Kls(23)		
print(ik.printd())
print(ik.smethod())
print(ik.cmethod())

print ('\n')

print(Kls.printd())
print(Kls.smethod())
print(Kls.cmethod())