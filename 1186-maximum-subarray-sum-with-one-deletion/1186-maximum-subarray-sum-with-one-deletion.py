class Solution:
    def maximumSum(self, arr):
        keep = arr[0]
        delete = 0
        ans = arr[0]

        for i in range(1, len(arr)):
            delete = max(keep, delete + arr[i])
            keep = max(arr[i], keep + arr[i])
            ans = max(ans, keep, delete)

        return ans
