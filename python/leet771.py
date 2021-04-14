class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        dict = {
            
        }
        
        
        for j in jewels: 
            dict[j] =0
        
        
        for s in stones:
            if s in dict:
                dict[s]+=1
        
        
        answer = 0
        
        for key in dict.keys():
            
            answer+= dict[key]
            
            
        return answer