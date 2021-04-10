class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height)==0: return 0
        answer =0
        
        l, r = 0, len(height)-1
        l_max, r_max = height[0], height[len(height)-1]
        
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            if r_max >= l_max:
                answer+=l_max-height[l]
                l+=1
            else:
                answer+=r_max-height[r]
                r-=1
            
        
        return answer