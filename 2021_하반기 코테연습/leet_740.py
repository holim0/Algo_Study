import copy
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        
        if len(nums)==1:
            return nums[0]
        
        num_max = max(nums)
        
        
        f = [0 for _ in range(num_max+1)]
        
        
        for n in nums:
            f[n]+=n
        
        
        dp = [0 for _ in range(num_max+1)]
        nums.sort()
        
        for n in range(1, num_max+1):
            
            if n==1:
                dp[n] = f[n]
            else:
                dp[n] = max(f[n]+dp[n-2], dp[n-1])
            
        print(dp)   
        
        
        
        return dp[num_max]
        
        
        
        
        