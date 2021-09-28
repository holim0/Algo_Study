from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y, n, m):
    
    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False



def solution(maps):
    answer = 0
    global dx, dy
    n = len(maps)
    m = len(maps[0])
    
    
    visit  = [[False for _ in range(m)] for _ in range(n)]
    
    q = deque([(0, 0, 1)])
    visit[0][0] = True
    while q:
        cx, cy, dist = q.popleft()
        
        if cx==n-1 and cy==m-1:
            answer = dist
            break
            
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            
            if check_range(nx, ny, n, m) and maps[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny, dist+1))
    
    if answer==0:
        return -1
    return answer