class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x) # convert the integer to a string
        return s == s[::-1] # check if the string is equal to its reverse
