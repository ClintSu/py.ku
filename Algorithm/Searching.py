# -*- coding:utf-8 -*- 

#顺序遍历-无序列表
#时间复杂度O(n)
def sequential_search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    return False

#二分查找-有序表查找
#时间复杂度O(log(n))
def binary_search(list,key):
    low=0
    high=len(list)-1
    time=0
    while low<high:
        time+=1
        mid=int((low+high)/2)
        print("mid=%s,low=%s,high=%s"%(mid,low,high))
        if key<list[mid]:
            high=mid-1
        elif key>list[mid]:
            low=mid+1
        else:
            # 打印折半的次数
            print("times: %s"%time)
            return mid
    if low==high:
        print("times: %s"%time)
        return low
    else:
        print("times: %s"%time)
        return False
#插值查找-有序表查找-待求证
#时间复杂度O(log(n))
def RPIM_search(list,key):
    low=0
    high=len(list)-1
    time=0
    while low<high:
        time+=1
        #计算mid值是插值算法的核心代码
        mid=low+int((key-list[low])/(list[high]-list[low])*(high-low))
        #mid=high-int((key-list[low])/(list[high]-list[low])*(high-low))
        print("mid=%s,low=%s,high=%s"%(mid,low,high))
        if key<list[mid]:
            high=mid-1
        elif key>list[mid]:
            low=mid+1
        else:
            #打印查找次数
            print("times: %s"%time)
            return mid
    if low==high:
        print("times: %s"%time)
        return low
    else:
        print("times: %s"%time)
        return False

#斐波那契查找-有序表查找
#时间复杂度O(log(2n))
def fibonacci_search(list,key):
    #需要一个现成的斐波那契列表。其中最大元素的值必须超过查找表中元素个数的数值。
    F=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]
    low=0
    high=len(list)-1

    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-high决定
    k=0
    while high>F[k]-1:
        k+=1
    print("F(index):%s"%k)
    i=high
    while F[k]-1>i:
        list.append(list[high])
        i+=1
    print(list)

    #算法主逻辑，time用于展示循环的次数。
    time=0
    while low<high:
        time+=1
        #为防止F列表下表益出，设置if和else
        if k<2:
            mid=low
        else:
            mid=low+F[k-1]-1
        print("low=%s, mid=%s, high=%s" % (low, mid, high))
        if key<list[mid]:
            high=mid-1
            k-=1
        elif key>list[mid]:
            low=mid+1
            k-=2
        else:
            if mid <= high:
                # 打印查找的次数
                print("times: %s" % time)
                return mid
            else:
                print("times: %s" % time)
                return high

    if low==high:
        print("times: %s"%time)
        return low
    else:
        print("times: %s"%time)
        return False

if __name__=='__main__':
    LIST1=[1,5,8,21,23,55,87,132,56,77,121,90]
    result1=sequential_search(LIST1,121)
    print(result1)
    LIST2 = [1, 5, 7, 8, 22, 34, 44, 45, 54, 99, 123,155, 200, 222, 444]
    result2 = binary_search(LIST2, 155)
    print(result2)    
    result3 = RPIM_search(LIST2, 155)
    print(result3)
    result4 = fibonacci_search(LIST2, 155)
    print(result4)
    