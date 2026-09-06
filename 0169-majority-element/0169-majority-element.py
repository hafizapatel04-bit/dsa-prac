class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:

            # If count becomes 0, choose a new candidate
            if count == 0:
                candidate = num

            # Same as candidate -> increase count
            if num == candidate:
                count += 1

            # Different from candidate -> cancel one vote
            else:
                count -= 1

        # Majority element always exists
        return candidate