#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 循环
print(range(3))
print(list(range(3)))

sum = 0
for x in range(101):
    sum += x
print(sum)


total = 0
n = 100
while n > 0:
    if n < 20:
        break
    total += n
    n -= 1

print(total)

i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(i)
    
