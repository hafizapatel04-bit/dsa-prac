class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        res = set()
        for x in nums2:
            if x in seen:
                res.add(x)
        return list(res)
        