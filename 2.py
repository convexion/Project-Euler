# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:32:12 2021

@author: Raj Saha
"""

f = [1,2]
n = 4000000
i = 1
sum = 0

while f[i] <= n:
    f.append(f[i] + f[i - 1])
    i += 1

for i in range(1, len(f), 3):
    sum = sum + f[i]

print(sum)