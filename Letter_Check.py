# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:24:50 2022

@author: saatvik
"""

def most_Frequent(arr, Len):
    d = {}
    for i in range(Len):
        if(arr[i] in d):
            d[arr[i]] = d[arr[i]] + 1
        else:
            d[arr[i]] = 1
    size = len(d)

    while (size > 0):
        currentMax = 0
        letter_max = 0
        for key, value in d.items():
            if (value > currentMax or (value == currentMax and key > letter_max)):
                letter_max = key
                currentMax = value
        
        print(f"{letter_max} - {currentMax}")
        d.pop(letter_max)
        size -= 1
 
Str = input("Enter a word: ")
Str1 = Str.casefold()
Len = len(Str)
most_Frequent(list(Str1), Len)
