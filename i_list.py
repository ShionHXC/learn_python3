#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 列表生成式
import os

print(list(range(1, 11)))

L = [x * x for x in list(range(1, 11))]
print(L)

# 仅返回偶数的平方list
L2 = [x * x for x in list(range(1, 11)) if x % 2 ==0]
print(L2)

# 使用两层循环，可以生成全排列：
L3 = [ m + n for m in 'ABC' for n in 'XYZ']
print(L3)

# 列出文件夹下所有文件
L4 = [d for d in os.listdir('.')]
print(L4)

L5 = { 'name': 'hxc', 'age': '18'}
for k,v in L5.items():
    print(k , '=' , v)

L6 = [k + '=' + v for k,v in L5.items()]
print(L6)

L7 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L7])

print(isinstance(123, int))
print(isinstance('123', str))


S1 = ['Hello', 'World', 18, 'Apple', None]
S2 = [x.lower() for x in S1 if isinstance(x, str)]

# 测试:
print(S2)
if S2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')