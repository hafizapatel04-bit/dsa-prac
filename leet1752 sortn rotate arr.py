# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 00:07:27 2026

@author: anamp
"""

class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False

        return True