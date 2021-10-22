from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        
        fre_cnt = defaultdict(int)
        
        
        for cur in s:
            fre_cnt[cur]+=1
            
        
        sorted_fre = sorted(fre_cnt.items(), key=lambda x: -x[1])
        
        answer =""
        
        for cur in sorted_fre:
            letter, cnt = cur
            
            for _ in range(cnt):
                answer+=letter
        
        return answer