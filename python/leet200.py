from collections import deque

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
    
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        
        answer  = 0
        
        visit = [[False] * m for _ in range(n)]
        def check_Range(x, y):
            
            if x>=0 and x<n and y>=0 and y<m:
                return True
            
            return False
            
        
        for i in range(n):
            for j in range(m):
                
                if visit[i][j]==False and grid[i][j]=="1":
                    visit[i][j] = True
                    answer+=1
                    q.append((i, j))
                    while q:    
                        curx, cury= q.popleft()
                        
                        for k in range(4):
                            nx, ny = curx +dx[k], cury+dy[k]
                            
                            if check_Range(nx, ny):
                                if grid[nx][ny]=="1" and not visit[nx][ny]:
                                    visit[nx][ny] = True
                                    q.append((nx, ny))
        
        
        return answer
                            
                            
                            
                            
                        
                        
                    
        