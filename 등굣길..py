def solution(m, n, puddles):
    answer = 0
    mod=1000000007
    check=[[False]*(m+2) for _ in range(n+2)]
    dp=[[0]*(m+2) for _ in range(n+2)]
    
    if len(puddles)>0:
        for a, b in puddles:
            check[b][a]=True
            
    dp[1][1]=1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1: continue   
            if check[i][j]==True:
                dp[i][j]=0
            
            else:
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
                
                            
    answer=dp[n][m]%mod
    
    return answer