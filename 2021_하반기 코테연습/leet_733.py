from collections import deque
class Solution:
    
    
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        
        
        def check_range(x,y):
            if x>=0 and x<n and y>=0 and y<m:
                return True
            return False
        
        
        visit = [[False for _ in range(m)] for _ in range(n)]
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        
        start_val = image[sr][sc]
        image[sr][sc] = newColor
        visit[sr][sc] = True
        
        
        q = deque([(sr, sc)])
        
        while q:
            
            cx, cy = q.popleft()
            
            for i in range(4):
                nx, ny = cx+dx[i], cy+dy[i]
                
                if check_range(nx, ny) and image[nx][ny]==start_val and not visit[nx][ny]:
                    visit[nx][ny] = True
                    image[nx][ny]=newColor
                    q.append((nx, ny))
                    
        
        
        return image
                    
    