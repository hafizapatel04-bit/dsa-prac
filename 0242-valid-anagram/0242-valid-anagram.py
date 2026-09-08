class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0) + 1
        for ch in t:
            count[ch] = count.get(ch,0) - 1
        for value in count.values():
            if value != 0:
                return False

        return True