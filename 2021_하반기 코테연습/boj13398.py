n = int(input())

number = list(map(int, input().split()))


dp = [[0 for _ in range(2)] for _ in range(n)]


dp[0][0] = number[0]


answer = -1e10


for i in range(1, n):
    
    dp[i][0] = max(dp[i-1][0]+number[i], number[i])


    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+number[i])

    answer= max(answer, max(dp[i][0], dp[i][1]))
    
if answer == -1e10:
    print(dp[0][0])
else:
    print(answer)



