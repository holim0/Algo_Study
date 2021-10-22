from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def check_range(x, y, n, m):
            if x>=0 and x<n and y>=0 and y<m:
                return True
            
            return False
            
        def check_border(cur, n, m):
            
            for c in cur:
                x, y = c
                
                if x==0 or x>=n-1 or y==0 or y>=m-1:
                    return False
                
            return True
        
        
        n, m = len(board), len(board[0])
        q = deque([])
        check = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                
                if board[i][j]=="O" and not check[i][j]:
                        q.append((i, j))
                        isOk = True
                        island = [(i, j)]
                        check[i][j] = True
                        while q:
                            cx, cy = q.popleft()
                            
                            for k in range(4):
                                nx, ny = cx+dx[k], cy+dy[k]
                                
                                if check_range(nx, ny, n, m) and board[nx][ny]=="O":
                                    if not check[nx][ny]:
                                        check[nx][ny] = True
                                        q.append((nx, ny))
                                        island.append((nx,ny))
                        
                        if check_border(island, n, m):
                            for l in island:
                                x, y = l
                                board[x][y] = "X"
                
                                
                    
                        
                        
                        