from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        
        n, m = len(grid), len(grid[0])

        check = [[False for _ in range(m)] for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i, j))
                    
        time = 0
        
        def check_range(x, y):
            if x>=0 and x<n and y>=0 and y<m:
                return True
            return False
        
        def check_done():
            
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1:return False
                    
            return True
        
        
        
        dx = [1,-1, 0, 0]
        dy = [0, 0, -1, 1]
        
        if len(q)==0:
            if check_done():
                return 0
        
       
        
        while q:
            
            size = len(q)
            
            if check_done():
                return time
            
            for _ in range(size):
                cx, cy = q.popleft()
                
                for i in range(4):
                    nx, ny = cx+dx[i], cy+dy[i]
                    
                    if check_range(nx, ny) and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx, ny))
            
            time+=1
        
        
        
        return -1