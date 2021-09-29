n = int(input())

MOD = 1000000000

dp = [[0 for _ in range(11)] for _ in range(n+1)]

## 길이 i에서 e로 끝나는 계단 수 갯수
dp[1][0] = 0

for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n+1):

    for e in range(0, 10):
        if e ==0:
            dp[i][e] = (dp[i-1][e+1])%MOD
        elif e==9:
            dp[i][e] = dp[i-1][e-1]%MOD
        else:
            dp[i][e] = (dp[i-1][e+1] + dp[i-1][e-1])%MOD





print(sum(dp[n])%MOD)

