from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        degree = [0] * numCourses
        link = [[] for _ in range(numCourses)]
        q = deque([])
        
        for p in prerequisites:
            a,b = p[0], p[1]
            degree[a]+=1
            link[b].append(a)
            
        
        for i in range(len(degree)):
            if degree[i]==0:
                q.append(i)
                
        if len(q)==0: return False
        
        
        while q:
            cur = q.popleft()
            
            
            for nxt in link[cur]:
                degree[nxt]-=1
                
                if degree[nxt]==0:
                    q.append(nxt)
                    
        
        for d in degree:
            if d!=0: return False
            
        return True