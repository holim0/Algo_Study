A = input()
B = input()

dp = [[0 for col in range(len(A)+1)] for row in range(len(B)+1)]


for i in range(len(B)):
    for j in range(len(A)):
        if A[j] == B[i]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[-1][-1])
