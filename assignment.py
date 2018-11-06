# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:00:24 2018

@author: laura
"""

def bubblesort(lst):
    
    for y in range(len(lst)-1):
        
        for x in range(len(lst)-y-1):
            if lst[x] > lst[x+1]:
                temp= lst[x]
                lst[x]=lst[x+1]
                lst[x+1]=temp
        
lst=[9,8,7,6,5,4]
bubblesort(lst)
print(lst)