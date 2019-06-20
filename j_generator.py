#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成器
L = [x * x for x in range(10)]
G = (x * x for x in range(10))
for n in G:
    print(n)


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a + b
        n = n + 1
    return 'done'
fib(10)

# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib1(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b, a + b
        n = n + 1
    return 'done'

f = fib1(3)
for n in f:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print('=========================')
for n in o:
    print(n)

# 拿到fid 的 return 值
# fibG = fib1(3)
print('==========================')
newF = fib1(3)
while True:
    try:
        x = next(newF)
        print('g:', x)
    except StopIteration as e:
        print('Return Value', e.value)
        break


# 杨氏三角
def triangles():
    p = [1]       
    while True:
       yield p         
       p =[1]+[p[x]+p[x+1] for x in range(len(p)-1)]+[1]

t = triangles()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))