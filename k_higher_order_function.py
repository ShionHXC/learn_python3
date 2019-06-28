#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 高阶函数
from functools import reduce
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

def f(x):
    return x * x

r = map(f, [1,2,3,4,5])
print(list(r))

s = map(str, [2,4,6,8])
print(list(s))

def add1(x,y):
    return x + y

sum = reduce(add1, [1,2,3,4,5])
print(sum)

# filter
def is_odd(x):
    return x % 2 == 1

odd = list(filter(is_odd, [1,2,3,4,5,6,7]))

print(odd)

def not_empty(x):
    return x and x.strip()
print(list(filter(not_empty, ['', 'ab ', ' ', 'c d'])))

# sorted()
print(sorted([-2,3,-55,98,3]))
print(sorted([-2,3,-55,98,3], key=abs)) # 安绝对值大小排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 忽略大小写  反序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(t):
    return t[0]
# 按成绩排序 从高到低
def by_score(t):
    return -t[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score))

# 匿名函数
print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f = lambda x: print(x * x)

f(5)
# 装饰器 写在函数前
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

def log(func):
    def wrap(*args, **kw):
        print('call %s:' % func.__name__)
        return func(*args, **kw)
    return wrap

@log
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
def now():
    print('2019-06-24')

# 拿到函数名字
print(now.__name__)

now()

# 装饰器本身需要传入参数
def log1(text):
    def decorator(func):
        def wrap(*args, **kw):
            print('%s %s()' %(text, func.__name__))
            return func(*args, **kw)
        return wrap
    return decorator

@log1('装饰器')
def today():
    print('今天是星期一')

today()