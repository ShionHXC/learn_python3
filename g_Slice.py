#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['a', 'b', 'c', 'd', 'e']
print(L[1:3]) # 从索引为1到索引为3 但不包括 3

print(L[-3: -1])
print(L[-3:])

LIST = list(range(100))

print(LIST[: 10]) # 取前十个
print(LIST[:10:2]) # 前十个 每两个取一个
print(LIST[::5]) # 全部 每5个取一个

S = 'Hello world'
print(S[:3])

print(S[::-1])

def trim(s):
    for i in s:
        if i == ' ':
            s = s[1:]
        else:
            break
    for i in s[::-1]:
        if i == ' ':
            s = s[:-1]
        else:
            break
    return s
print(trim(' hello world  '))