# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 22:36:22 2026

@author: anamp
"""

def getElements(arr, n):
    if n == 0 or n==1:
        print(-1,-1)
        return 
    
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
        
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print ("second smallest is", second_small)
    print ("2nd largest is", second_large)
    
    #driver code
if __name__ == "__main__":
    
    arr = [7,7,2,5,2,10,10,10]
    n = len(arr)
    getElements(arr, n)