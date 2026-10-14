class Solution(object):
    def maxSubArray(self, nums):
        
        best = nums[0]
        max1 = nums[0]

        for num in nums[1:]:
            best = max(num, best + num)
            max1 = max(max1, best)
        return max1


        

