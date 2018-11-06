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

#%%
def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            
    if len(left) == 0:
        result += right
    else:
        result += left
            
    return result
        
# merge sort implementation
#
# this function uses our previously declared function merge
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    return merge(merge_sort(left), merge_sort(right))