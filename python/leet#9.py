class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)

        for i in range(len(s)//2):

            if s[i] != s[len(s)-i-1]:
                return False

        return True
