class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        list_s1 = list(s1)
        list_s1.sort()
        size = len(s1)
        sort_s1 = "".join(list_s1)
        
        for i in range(len(s2)-size+1):
            cur = s2[i:i+size]
            
            cur = list(cur)
            cur.sort()
            cur = "".join(cur)
            
            if cur==sort_s1: return True
            
            
        return False
        