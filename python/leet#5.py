class Solution:
    def longestPalindrome(self, s: str) -> str:

        size = len(s)

        dp = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = 1

        a, b = 0, 0
        l = 1
        for i in range(size-1):
            if s[i] == s[i+1]:
                a, b = i, i+1
                l = 2
                dp[i][i+1] = 1

        for i in range(3, size+1):
            for j in range(size-i+1):
                if s[j] == s[j+i-1] and dp[j+1][j+i-2] == 1:
                    dp[j][j+i-1] = 1
                    if l < i:
                        l = i
                        a = j
                        b = j+i-1

        return s[a:b+1]
