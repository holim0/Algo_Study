import sys
n = int(input())

arr = list(map(int, input().split()))

m = int(input())


dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1


for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for l in range(3, n+1):
    for i in range(0, n-l+1):
        if arr[i] == arr[i+l-1] and dp[i+1][i+l-2] == 1:
            dp[i][i+l-1] = 1


for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
