#!/usr/bin/python 
# -*- coding:utf-8 -*-

__author__ = 'clint'
__date__ = '2017-08-30'

class Node():
    #限定Node实例的属性
    __slots__=['_item','_next']
     #Node的指针部分默认执行None  
    def __init__(self,item):
        self._item=item
        self._next=None 
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newItem):
        self._item=newItem
    def setNext(self,newNext):
        self._next=newNext

class SingleLinkedList():
    #初始化空单链表
    def __init__(self):
        self._head=None  
        self._size=0
    def isEmpty(self):
        return self._head==None
    def size(self):
        current=self._head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def printd(self):
        current=self._head
        while current!=None:
            print (current.getItem())
            current=current.getNext()
    def add(self,item):
        temp=Node(item)
        temp.setNext(self._head)
        self._head=temp
    def append(self,item):
        temp=Node(item)
        #若为空表，将添加的元素设为第一个元素
        if self.isEmpty():
            self._head=temp 
        else:
            current=self._head
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
    def search(self,item):
        current=self._head
        foundItem=False
        while current!=None and not foundItem:
            if current.getItem()==item:
                foundItem=True
            else:
                current=current.getNext()
        return foundItem
    def index(self,item):
        current=self._head
        count=0
        found=None
        while current!=None and not found:
            count+=1
            if current.getItem()==item:
                found=True
            else:
                current=current.getNext()
        if found:
            return found
        else:
            raise (ValueError,'%s is not in linkedlist'%item)
    def insert(self,pos,item):
        if pos<=1:
            sef.add(item)
        elif pos>self.size():
            self.append(item)
        else:
            temp=Node(item)
            count=1
            pre=None
            current=self._head
            while count<pos:
                count+=1
                pre=current
                current=current.getNext()
            pre.setNext(temp)
            temp.setNext(current)
    def remove(self,item):
        current=self._head
        pre=None
        while current!=None:
            if current.getItem()==item:
                if not pre:
                    self._head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre=current
                current=current.getNext()

def funcname(self, parameter_list):
    raise NotImplementedError

if __name__=='__main__':
    l=SingleLinkedList()
    for i in range(1,10):
        l.append(i)
    print (l.size())
    l.printd()
    print (l.search(6))
    print (l.index(5))

    l.remove(4)
    l.printd()
    l.insert(4,100)
    l.printd()