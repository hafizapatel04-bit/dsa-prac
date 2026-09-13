class Solution(object):
    def pivotIndex(self, nums):

        # Calculate total sum of the array
        total = sum(nums)

        # Sum of elements to the left
        left_sum = 0

        # Check every index
        for i in range(len(nums)):

            # Calculate right sum
            right_sum = total - left_sum - nums[i]

            # Check if left and right are equal
            if left_sum == right_sum:
                return i

            # Add current element to left sum
            left_sum += nums[i]

        # No pivot found
        return -1