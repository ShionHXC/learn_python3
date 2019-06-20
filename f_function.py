#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from my_function import my_abs
print(my_abs(-5))

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

x,y = move(100, 100, 5, math.pi / 6)
print(x, y)

# 可变参数
def calc(*number):
    sum = 0
    for n in number:
        sum += n
    return sum

sum = calc(1,2,3)

nums = [1,2,3,4,5]

print(*nums)
print(sum)
print(calc(*nums))

# 关键字参数
def person(age, name, **kw):
    print('age', age, 'name', name, 'other:', kw)

person(18, 'hxc', city='hangzhou')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person(29, 'zsy', **extra)

# 命名关键字参数






