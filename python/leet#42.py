
# 투포인터로 다시 풀기
class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        
        
        for i in range(1, len(height)-1):
            leftMax = max(height[:i])
            rightMax = max(height[i+1:])
            
            if leftMax <= height[i] or rightMax <= height[i]:
                continue
                
                
            else:
                smaller = min(leftMax, rightMax)
                answer+=smaller-height[i]
            
        
        
        
        return answer