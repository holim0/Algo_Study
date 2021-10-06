class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
        
        INF = -1e10
        n = len(nums)
        
        if n==1:
            return nums[0]
        
        dp =[0 for _ in range(n)]
        
        
        dp[0] = nums[0]
        dp[1] = INF
        dp[-1] = INF
        
        answer = nums[0]
        
        for i in range(2,n-1):
            
            dp[i] = max(dp[:i-1]) + nums[i]
            
            
        answer = max(dp)
        
        
        dp = [0 for _ in range(n)]
        
        dp[0] = INF
        dp[1] = nums[1]
        
        answer =max(answer, dp[1])
        
        
        for i in range(2, n):
            val= max(dp[:i-1])
            if val==INF:
                dp[i] = nums[i]
            else:
                dp[i] = val+nums[i]
            
        
        answer = max(answer, max(dp))
        
        return answer
            
        
        
        