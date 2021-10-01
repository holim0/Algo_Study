from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        d =defaultdict(int)
        
        
        for i in range(len(nums)):
            
            if nums[i] > 0:
                d[nums[i]]=1
                
        max_val = max(nums)
        
        if max_val<=0:
            return 1
        
        
        for i in range(1, max_val+2):
            
            if d[i]==0:
                
                return i