import sys
n = int(input())

mat = []

dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i]=0


for i in range(n):
    r, c= map(int, input().split())
    mat.append((r, c))


for i in range(n-1):
    r1, c1 = mat[i]
    r2, c2 = mat[i+1]

    dp[i][i+1] = r1 * c1 * c2


for l in range(3,n+1):
    for i in range(n-l+1):
        start= i
        end = i+l-1
        for j in range(start, end):
            r1 = mat[start][0]
            c1 = mat[j][1]
            c2 = mat[end][1]
            cost = dp[i][j] + dp[j+1][i+l-1] + r1 *c1 *c2
            dp[i][i+l-1]  = min(dp[i][i+l-1], cost)

print(dp[0][n-1])

