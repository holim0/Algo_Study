from functools import update_wrapper
import sys
input = sys.stdin.readline

t = int(input())

while t:


    n = int(input())

    sti = []

    for _ in range(2):
        tmp = list(map(int, input().split()))
        sti.append(tmp)

    dp = [[0 for _ in range(n)] for _ in range(2)]


    dp[0][0] = sti[0][0]
    dp[1][0] = sti[1][0]
    if n>1:
        dp[0][1] = dp[1][0]+sti[0][1]
        dp[1][1] = dp[0][0] + sti[1][1]
        
        for i in range(2, n):
            
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) +sti[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sti[1][i]

    

    print(max(dp[0][-1], dp[1][-1]))


    t-=1