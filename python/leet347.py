class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt ={}
        
        answer = []
        
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n]+=1
                
                
        sorted_cnt = sorted(cnt.items(), key =lambda x : x[1], reverse= True)
        
        for i in range(k):
            key, val = sorted_cnt[i]
            
            
           
            answer.append(key)
                
                
                
        return answer