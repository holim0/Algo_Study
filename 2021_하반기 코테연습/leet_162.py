from collections import defaultdict
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        withIdx = []
        
        idx_dict = defaultdict(int)
        
        for i in range(len(nums)):
            withIdx.append((nums[i], i))
            idx_dict[i] = nums[i]
            
        
        withIdx.sort()
        
        l, r = 0, len(withIdx)-1
        
        while l<=r:
            
            mid = (l+r)//2
            
            cur_value, cur_idx = withIdx[mid]
            
            
            if cur_idx-1>=0 and cur_idx+1<len(withIdx):
                
                if cur_value > idx_dict[cur_idx-1] and cur_value >idx_dict[cur_idx+1]:
                    return cur_idx
                
            elif cur_idx ==len(withIdx)-1:
                if cur_value> idx_dict[cur_idx-1]:
                    return cur_idx
                
            elif cur_idx==0:
                if cur_value >idx_dict[1]:
                    return 0
                
            
            l = mid+1
            
        return 0