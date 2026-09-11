class Solution(object):
    def longestCommonPrefix(self, strs):

        # Start with the first string as our prefix
        prefix = strs[0]

        # Compare it with every other string
        for i in range(1, len(strs)):

            # Keep reducing prefix until current string
            # starts with the prefix
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                # No common prefix
                if prefix == "":
                    return ""

        return prefix