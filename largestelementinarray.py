# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 22:09:33 2026

@author: anamp
"""

nums = [-4, -3, 0, 1, -8]

max_value = nums[0]
for i in range(1, len(nums)):
    if nums[i] > max_value:
        max_value = nums[i]

print(max_value)