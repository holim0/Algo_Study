from collections import deque
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check_range(x, y, n, m):
        
            if x>=0 and x<n and y>=0 and y<m:
                return True
        
            return False
        
        answer = 0
        m = len(grid[0])
        
        n = len(grid)
        
        q = deque([])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        visit = [[False for _ in range(m)] for _ in range(n)]
        
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1 and not visit[i][j]:
                    visit[i][j] = True
                    
                    q.append((i, j, 4))
                    
                    while q:
                        cx, cy, cnt = q.popleft()
                        
                        for k in range(4):
                            nx, ny = cx+dx[k], cy+dy[k]
                            
                            if check_range(nx, ny, n, m) and grid[nx][ny]==1:
                                cnt-=1
                                if not visit[nx][ny]:
                                    visit[nx][ny] = True
                                    q.append((nx, ny, 4))
                                
                        
                        answer+=cnt
                        
                        
                        
                        
        return answer
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        