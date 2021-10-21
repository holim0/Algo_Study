class Solution:
    def jump(self, nums):
        
        INF = 1e10
        dp = [INF] * len(nums)
        
        
        dp[0] = 0
        
        
        for i in range(len(nums)):
            for j in range(i+1, i+nums[i]+1):
                if j<len(nums):
                    dp[j] = min(dp[j], dp[i]+1)
        
        
        
        

        return dp[len(nums)-1]