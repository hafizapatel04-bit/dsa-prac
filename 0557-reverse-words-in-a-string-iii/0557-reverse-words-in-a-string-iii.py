class Solution(object):
    def reverseWords(self, s):

        # Split sentence into individual words
        words = s.split()

        # Reverse every word
        for i in range(len(words)):
            words[i] = words[i][::-1]

        # Join words back with spaces
        return " ".join(words)