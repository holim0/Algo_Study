from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        n, m = len(grid), len(grid[0])
        q = deque([])
        visit = [[False for _ in range(m)] for _ in range(n)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def check_range(x, y):
            if x>=0 and x<n and y>=0 and y<m:
                return True
            
            return False
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visit[i][j]:
                    tmp = 1
                    visit[i][j] = True
                    q.append((i, j))
                    
                    while q:
                        cx,cy = q.popleft()
                        
                        for k in range(4):
                            nx, ny = cx+dx[k], cy+dy[k]
                            
                            if check_range(nx, ny) and grid[nx][ny]==1 and not visit[nx][ny]:
                                tmp+=1
                                visit[nx][ny] = True
                                q.append((nx, ny))
                                
                    answer = max(answer, tmp)
    
        
    
        
        
        return answer