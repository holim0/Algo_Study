import sys
n, s, m = map(int, input().split())

dp = [[False for _ in range(m+1)] for _ in range(n)]


vol = list(map(int, input().split()))


up = s + vol[0]
down = s-vol[0]

if up <= m:
    dp[0][up] = True

if down >= 0:
    dp[0][down] = True


for i in range(1, n):
    for j in range(m+1):
        if dp[i-1][j]:
            up = j+vol[i]
            down = j-vol[i]
            if up <= m:
                dp[i][up] = True
            if down >= 0:
                dp[i][down] = True

answer = -1

for i in range(m+1):

    if dp[n-1][i]:
        answer = max(answer, i)


print(answer)
