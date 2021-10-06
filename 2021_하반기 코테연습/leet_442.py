from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        
        dic = defaultdict(int)
        
        for n in nums:
            dic[n]+=1
            
            if dic[n]==2:
                answer.append(n)
                
        
        return answer