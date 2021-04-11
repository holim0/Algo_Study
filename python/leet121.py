import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = -sys.maxsize
        
        s = []
        
        s.append(prices[0])
        
        for i in range(1, len(prices)):
            if prices[i] < s[-1]:
                s.pop()
                s.append(prices[i])
                
            else:
                answer =max(answer, prices[i]-s[-1])
            
        
        if answer<=0: 
            return 0
        
        else:
            return answer
            