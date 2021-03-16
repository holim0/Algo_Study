class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        s = list(s)

        for i in range(len(s)):
            if not s[i].isdigit() and not s[i].isalpha():
                s[i] = ""

        result = ""

        for i in range(len(s)):
            if s[i].isdigit() or s[i].isalpha():
                result += s[i]

        for i in range(len(result)//2):
            if result[i] != result[len(result)-i-1]:
                return False

        return True
