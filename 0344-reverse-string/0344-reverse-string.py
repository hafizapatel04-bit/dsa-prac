class Solution(object):
    def reverseString(self, s):
        result = []
        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])

        # Copy back into original array
        for i in range(len(s)):
            s[i] = result[i]
        