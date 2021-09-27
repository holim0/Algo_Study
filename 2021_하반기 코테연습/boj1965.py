n = int(input())

number= list(map(int, input().split()))

dp = [0 for _ in range(n)]

dp[0]= 1

for i in range(1, n):
    cur = number[i]
    
    max_dp = -1
    max_val = -1
    for j in range(i-1, -1, -1):
        if number[j]<cur:
            max_dp = max(max_dp, dp[j])
        

    if max_dp==-1:
        dp[i] = 1
    else:
        dp[i] = max_dp+1






print(max(dp))



