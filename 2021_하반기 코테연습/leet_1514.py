import heapq as hp

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        
        link = [[] for _ in range(n+1)]
        
        for i in range(len(edges)):
            f, to = edges[i][0], edges[i][1]
            w = succProb[i]
            link[f].append((to, w))
            link[to].append((f, w))
                
        
        def getSol(start, end):
            
            dist = [-1 for _ in range(n+1)]
            
            dist[start] = 0
            
            q = []
            
            hp.heappush(q, (0, start))
            
            
            while q:
                cur_dist, cur = hp.heappop(q)
                
                
                if dist[cur]> -cur_dist: continue
                
                
                for i in link[cur]:
                    to, d = i
                    next_dist = None
                    if cur_dist==0:
                        next_dist = d
                    else:
                        next_dist = d * (-cur_dist)
                    
                    if next_dist > float(dist[to]):
                        
                        dist[to] = next_dist
                        hp.heappush(q, (-next_dist, to))
                    
            return dist[end]
              
        
            
            
        
        tmp = getSol(start, end)
       
        if tmp==-1:
            return 0

        else:
            return tmp
                
                
            
        
        
        
        