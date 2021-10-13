class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        answer = []
        def getsol(idx, cur):
            
            if len(cur) == len(s):
                answer.append(cur)
                return 
            
            
            if s[idx].isalpha():
                lower = s[idx].lower()
                getsol(idx+1, cur+lower)
                
                upper = s[idx].upper()
                getsol(idx+1, cur+upper)
                
            else:
                getsol(idx+1, cur+s[idx])
            
            
            
        
        getsol(0, "")
        
        return answer