#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 30
if age < 12:
    print('儿童')
elif age < 18:
    print('高中')
elif age < 29:
    print('90后老年人')
else:
    print('大哥好')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00后')
else:
    print('00前')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = float(input('身高：'))
weight = float(input('体重：'))
BMI = float('%.2f' % (weight / (height**2)))
print('BMI指数：', BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
