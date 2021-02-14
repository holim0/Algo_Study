import sys
import math
input = sys.stdin.readline
t = int(input())
maxValue = 987654321
while t:

    k = int(input())

    file = list(map(int, input().split()))
    dp = [[0] * (k+1) for _ in range(k+1)]

    acc = list(file)

    for i in range(1, k):
        acc[i] = acc[i-1]+acc[i]

    for i in range(2, k + 1):
        for s in range(k-i+1):

            end = s+i-1
            dp[s][end] = math.inf

            for j in range(s, end+1):
                if s == 0:
                    sum_val = acc[end]
                else:
                    sum_val = acc[end]-acc[s-1]
                dp[s][end] = min(dp[s][end], dp[s][j]+dp[j+1][end] + sum_val)

    print(dp[0][k-1])

    t -= 1
