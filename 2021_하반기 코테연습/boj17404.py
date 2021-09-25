n = int(input())

mapp = []
INF = 987654321
dp =[[INF for _ in range(3)] for _ in range(n)]



for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)




## 0으로 시작



answer= 987654321
    
for k in range(3):
    dp =[[INF for _ in range(3)] for _ in range(n)]
    dp[0][k] = mapp[0][k]
    
    for i in range(1, n):
        if i==n-1:
            if k ==0:
                dp[i][0] = INF
                dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + mapp[i][1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + mapp[i][2]

            if k ==1:
                dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + mapp[i][0]
                dp[i][1] = INF
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + mapp[i][2]

            if k ==2:
                dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + mapp[i][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + mapp[i][1]
                dp[i][2] = INF

        

        else:
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + mapp[i][0]

            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + mapp[i][1]

            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + mapp[i][2]


    tmp= min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2])
    answer = min(answer, tmp)


print(answer)