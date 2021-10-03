class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        size = len(nums)
        
        if size==1:
            return 0
        
        sum_front = [nums[0]]
        
        sum_back = [nums[-1]]
        
        
        for i in range(1,size):
            tmp = nums[i] + sum_front[-1]
            sum_front.append(tmp)
            
        for i in range(size-2, -1, -1):
            tmp = nums[i] + sum_back[-1]
            sum_back.append(tmp)
            
        sum_back= sum_back[::-1]
        sum_back.append(0)
        
        for i in range(size):
            left_sum, right_sum = -1, -1
            if i==0:
                left_sum = 0
                right_sum = sum_back[i+1]
                
            elif i==size-1:
                left_sum = sum_front[i-1]
                right_sum = 0
            
            else:
                left_sum = sum_front[i-1]
                right_sum = sum_back[i+1]
            
            if left_sum==right_sum:
                    return i
        
        
        return -1