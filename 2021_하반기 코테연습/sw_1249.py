from collections import deque

def check_range(x, y, n):
   if x>=0 and x<n and y>=0 and y<n: return True
   return False

INF  = 1e10

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    mapp = []
    answer = 1e10
    visit = [[INF for _ in range(n)] for _ in range(n)]
    
    for _ in range(n):
        tmp = input()
        arr = []
        for t in tmp:
            arr.append(int(t))
        mapp.append(arr)
    
    visit[0][0] = 0
    sx, sy = 0, 0
    
    q = deque([(0, 0, 0)])
   
    while len(q)>0:
       
        cx, cy, weight = q.popleft()
        
        if cx==n-1 and cy==n-1:
            answer = min(answer, weight)
            
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            
            if check_range(nx, ny, n):
                if visit[nx][ny] > mapp[nx][ny]+weight:
                    visit[nx][ny] = mapp[nx][ny] +weight
                    q.append((nx, ny, mapp[nx][ny]+weight))
       
        
    print("#{t} {v}".format(t=test_case, v=visit[n-1][n-1]))