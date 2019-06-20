#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 10,
    'Bob': 20
}
print(d.get('Bob'))
print(d.get('Jane'))
print(d.get('Jane', -1)) # 为None时  指定返回值
d['Jane'] = 'new'
d.pop('Bob')
print(d)

s = set([1,2,3,3,4])
print(s)
s.add(5)
print(s)
s.remove(2)
print(s)