# -*- coding: utf-8 -*-
"""

Left Rotate the Array by One





Problem Statement: Given an integer array nums, rotate the array to the left by one.

"""

class solution:
    def rotatearraybyone(self, arr):
        #storing the temp variable
        temp = arr[0]
        #shift elements to the left
        for i in range(1, len(arr)):
            arr[i-1] = arr[i]
            
            #place the first element at end
            arr[-1] = temp
#main method for testing
if __name__ =='__main__':
    solution = Solution()
    arr = [1,2,3,4,5]
    
    solution.rotatearraybyone(arr)
    print(arr)

        