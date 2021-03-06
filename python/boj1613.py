import sys
n, k = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


for i in range(k):
    n1, n2 = map(int, sys.stdin.readline().split())
    dp[n1][n2] = -1
    dp[n2][n1] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] == 0:
                if dp[i][k] == 1 and dp[k][j] == 1:
                    dp[i][j] = 1
                    dp[j][i] = -1
                elif dp[i][k] == -1 and dp[k][j] == -1:
                    dp[i][j] = -1
                    dp[j][i] = 1


s = int(input())

for i in range(s):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(dp[n1][n2])
