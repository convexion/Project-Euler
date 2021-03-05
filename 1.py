# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:25:13 2021

@author: Raj Saha
"""

def compute(n, m1, m2):
    for i in range(m1):
        if ((n - 1) - i)%(m1) == 0:
            l1 = ((n - 1) - i)/(m1)
    for i in range(m2):
        if ((n - 1) - i)%(m2) == 0:
            l2 = ((n - 1) - i)/(m2)
    for i in range(m1*m2):
        if ((n - 1) - i)%((m1*m2)) == 0:
            l3 = ((n - 1) - i)/((m1*m2))
    sum = m1*l1*(l1 + 1)/2 + m2*l2*(l2 + 1)/2 - (m1*m2)*l3*(l3 + 1)/2
    return int(sum)

n = 1000
m1 = 3
m2 = 5
sum = compute(n, m1, m2)
print(sum)