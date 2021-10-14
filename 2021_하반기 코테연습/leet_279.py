class Solution:
    def numSquares(self, n: int) -> int:
        
        INF = 1e10
        dp = [INF for _ in range(n+1)]
        
        dp[0]=0
        dp[1]=1
        
        squa = []
        k =1
        while k**2<=n:
            squa.append(k**2)
            k+=1
        
        for i in range(2, n+1):            
            for s in squa:
                if i-s>=0:
                    if dp[i] > dp[i-s]+1:
                        dp[i] = dp[i-s]+1
                   
        
            
        
        
        return dp[n]
            
            
            
        