class Solution(object):
    def isPalindrome(self, x):

        # Negative numbers are not palindromes
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:

            # Get the last digit
            digit = x % 10

            # Add digit to reverse
            reverse = reverse * 10 + digit

            # Remove last digit
            x = x // 10

        # Compare original and reversed number
        return original == reverse