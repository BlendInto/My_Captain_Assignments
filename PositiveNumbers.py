# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:58:35 2022

@author: saatvik
"""

list = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    element = int(input("Enter element: "))
    list.append(element)
x = 0
print("The positive numbers are: ")
while x < n:
    if(list[x]>0):
        print(list[x])
        x+=1
    elif(list[x]<0):
        x+=1
        continue
    elif(x == n):
        break
        