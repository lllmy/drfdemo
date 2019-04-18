from django.test import TestCase

# Create your tests here.
# class A:
#     B=1
#     def foo(action=None,**kwargs):
#         print(2222)
#         print(111)
#         return 333
#
#
# print(getattr(A,'foo')())
# 一行代码实现9*9乘法表
# print('\n'.join(['\t'.join(["%s*%s=%s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))


# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%s*%s=%s" % (y,x,x*y),end=' ')
#     print() # print默认参数‘换行’，没有此条语句输出打印时将不会换行
# print(( i % 2 for i in range(10) ))
# print(1 < 2 == 2)
# s="1,2,3"
# l1=s.split(",")
# print(l1)
# a=['1','2','3']
# b=[int(i) for i in a]
# print(b)
# a = ["1", "2", "3"]
# # b = [int(x) for x in a]
# print(list(map(lambda x: int(x), a)))
# 45.如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] ?
# print([i**2 for i in range(0,11)])
# l = [2, 3, 5, 10, 15, 33, 55]
# def two_search(li, aim, start=0, end=None):
#     end = len(li)-1 if end is None else end
#     mid_index = (end - start) // 2 + start  # 3
#     if start <= end:
#         if li[mid_index] < aim:
#             return two_search(li, aim, start=mid_index+1, end=end)
#         elif li[mid_index] > aim:
#             return two_search(li, aim, start=start, end=mid_index-1)  #（[2,3,5],3）
#         elif li[mid_index] == aim:
#             return mid_index
#         else:
#             return '没有此值'
#     else:
#         return '没有此值'
# print(two_search(l,100))
# new_l = []
# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             if i!=j and j!=k and i!=k:
#                 new_l.append('%s%s%s'%(i,j,k))
# print(len(new_l))
# l = [1, 2, 3, 4, 5]
# new_l = []
# for i in l:
#     for j in l:
#         for k in l:
#             if i !=j and j!=k and i!=k:
#                 new_l.append('%s%s%s'%(i,j,k))
# print('能组成的互不相同且无重复数字的三位数：%s'%(len(new_l)))
# nums =[2,7,11,15]
# class Searching(object):
#     def sum(self,nums,target):
#         if len(nums)<=1:
#             return False
#         dics= {}
#         for i in range(len(nums)):
#             if nums[i] in dics:
#                 return [dics[nums[i]],i]
#             else:
#                 dics[target-nums[i]]=i
# s=Searching()
# print(s.sum(nums,13))
from sys import getrefcount
# a=[1,2,3]  # 赋值
# b=a  # 又一次
# c=[4,a]  # 又一次 共三次了
# # 相当于给a的引用计数-1
# del b   # 减一次
# c.remove(a) # 又减一次
# print(getrefcount(a)) # 增加一次
# 引用计数增加的情况
# 赋值
# 引用
# 当成函数参数传递给函数
# 引用被显性或者隐性的删除
# 函数结束的时候里面参数的引用计数会减一

# 当这个对象的引用计数为0的时候 我们就认为它是垃圾可以被回收
a = [1,2,3,4]
b = [5,6,7]
a.append(b)
b.append(a)

print(getrefcount(a))  # 3
print(getrefcount(b))  # 3
# 解决循环引用的问题
# 标记清除
# 孤立的循环引用
# 在内存中找根节点  全局变量
# 以全局变量出发 可以找到所有可达对象
# 所有不可达对象就是垃圾

# 效率问题
# 分代回收
# 时间换空间
# 在内存中存活时间越长 越不可能是垃圾
# 0代 最年轻的一代  链表
# 当0代对象达到一个标准的时候我们就去触发垃圾回收
# 触发引用计数 在去做标记清除
# 我就把0代存活放入1代
# 当我们0代触发10次的时候 就触发1代的回收
# 1代被回收 存活的对象放入2代
# 当1代触发10次 触发2代回收

a = [1, 2]
b = [1, 2]
c = 1
d = 1

# python自己维护内存池
# 跟c的接口 去开辟内存空间
# 700 调用c接口开辟内存跟销毁内存的次数差值


# 总结
# 引用计数为主
    # 引用计数增加和减少一些情况
    # 当引用计数为0 代表是垃圾要被回收
# 标记清除 分代回收为辅
    # 标记清除解决孤立的循环引用
    # 分代回收解决效率问题
        # 阈值  3代（700， 10， 10）
# C3算法 归并算法
class A(object): pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(C): pass
class F(D, E): pass

print(F.__mro__)
# 第一步先找到继承的父类的MRO
# D = [D, B, A, O]
# E = [E, C, A, O]
# 第二步 把父类这两个MRO 和 DE 进行归并
# 取每个表表头 并且其他表去掉表头的部分不能含有我们要取的那个表头
# 如果不满走就去取第二个表头
# merge([DBAO], [ECAO], [DE])
# FD merge([BAO], [ECAO], [E])
# FDB merge([AO], [ECAO], [E])
# FDBE merge([AO], [CAO])
# FDBEC merge([AO], [AO])
# FDBECAO

# merge([AO], [OA])