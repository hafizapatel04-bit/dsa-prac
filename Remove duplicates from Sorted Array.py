'''Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

'''

class solution :
    def removedulicates(self, nums):
        if not nums:
            return 0
        # pointer to last unique element 
        i = 0
        # traverse the list starting from second element
        for j in range(1, len(nums)):
            # if current element is diff from last unique one
            if nums[j] != nums[i]:
                #move pointer forword
                i = i+1
                # place the unique element in next position
                nums[i] = nums[j]
        # i is last index of unoque elenment  , count = i+1
        return i + 1
    
nums = [1,1,2,2,2,3,3]
sol = solution()
k = sol.removedulicates(nums)
print('unique  counr =', k)
print("array after removing du[plicates ", nums[:k])
        