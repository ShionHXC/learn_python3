#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
dic = {'a': 1, 'b': 2, 'c': 3}
for key in dic:
    print(key)

for value in dic.values():
    print(value)

for k,v in dic.items():
    print(k,v)

# 迭代字符串
s = '你好'
for i in s:
    print(i)

print(isinstance(s, Iterable))
print(isinstance(123, Iterable)) # 整数不可迭代

for i,v in enumerate(['a', 'b', 'c']):
    print(i,v)

for (x,y) in [(1,2), (2,4)]:
    print(x,y)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) > 0:
        max = min = L[0]
        for i in L:
            if i > max:
                max = i
            elif i < min:
                min = i
        return (min, max)
    else:
        return (None, None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功5!')
