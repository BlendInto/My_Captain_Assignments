# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:14:23 2022

@author: saatv
"""
n = -1
x = 0
y = 1
z = 0

while True:
    x = 0
    y = 1
    z = 0
    n = int(input("Enter limit of Fibonacci series: "))
    if(n>0):
        print (x)
        print (y)
        while z<=n:
            z = x + y
            x = y
            y = z
            print(z)
    else:
        print("Invalid value of limit")
        break
        
    