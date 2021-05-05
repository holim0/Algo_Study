n, m = map(int, input().split())

number= []
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    tmp = input()
    tmp = list(map(int, tmp))

    number.append(tmp)




for i in range(n):
    for j in range(m):
        if number[i][j]==1: dp[i][j]=1


for i in range(n):
    for j in range(m):
        if number[i][j]==1:

            if i>0 and j>0:
                if dp[i-1][j-1]!=0 and dp[i-1][j]!=0 and dp[i][j-1]!=0:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))+1
                    

            


answer = 0


for i in range(n):
    tmp = max(dp[i])
    answer= max(tmp, answer)

print(answer * answer)

