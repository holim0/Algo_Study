import sys
n, k = map(int, input().split())


weight = []


for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weight.append((w, v))


dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


for i in range(1, n+1):

    curWeight, curValue = weight[i-1]

    for j in range(k+1):
        if curWeight <= j:
            dp[i][j] = max(curValue+dp[i-1][j-curWeight], dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j]


answer = max(map(max, dp))

print(answer)
