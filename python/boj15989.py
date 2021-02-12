t = int(input())


dp = [[0] * 3 for _ in range(10001)]

dp[1][0] = 1

dp[2][0] = 1
dp[2][1] = 1

dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, 10001):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]


for i in range(t):
    tmp = int(input())
    print(dp[tmp][0] + dp[tmp][1] + dp[tmp][2])
