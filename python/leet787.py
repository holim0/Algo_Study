from collections import deque
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        q = deque([])
        
        dict ={}
        
        min_answer= sys.maxsize
        
        visit = [[False for _ in range(n)] for _ in range(n)]
        
        
        for f in flights:
            u, v, w = f[0], f[1], f[2]
            
            if u not in dict:
                dict[u] = [(v, w)]
                
            else:
                dict[u].append((v, w))
                
            
        visit = {
            src : 0
        }
            
            
        q.append((src, 0, 0))
        
        while q:
            cur, stops, weight = q.popleft()
            
            if cur == dst and stops-1<=K:
                min_answer= min(min_answer, weight)
            
            if cur in dict:
                for next_target in dict[cur]:
                    next_n, next_weight = next_target
                    if next_n not in visit or visit[next_n]> weight+next_weight:
                        visit[next_n] = weight+next_weight
                        q.append((next_n, stops+1, weight+next_weight))

                    
                        
                        
                    
                    
        if min_answer== sys.maxsize:
            return -1
        
        return min_answer
                    
                    
                    
                    