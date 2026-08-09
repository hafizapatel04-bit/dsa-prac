class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        low = 0
        high = 0
        result = float('inf')
        total = 0

        while (high < n):
            total = total + nums[high]

            while (total >= target):
                leng = high - low + 1
                result = min(result, leng)
                total = total - nums[low]
                low += 1
            high +=1
        if result == float('inf'):
            return 0
        return result