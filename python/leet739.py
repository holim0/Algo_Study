class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        s = []
        answer= [0 for _ in range(len(T))]
        
        for i in range(len(T)):
            
            if len(s)==0:
                s.append((T[i], i))
            
            else:
                while True:
                    if len(s)==0:
                        s.append((T[i], i))
                        break
                    
                    value, idx = s[-1]
                    if T[i]> value:  
                        s.pop()
                        answer[idx] = i-idx
                    else:
                        s.append((T[i], i))
                        break
                
               
        return answer