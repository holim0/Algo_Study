from collections import deque
n, m = map(int, input().split())

mapp = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

q = deque([])

answer = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = -1, -1

for i in range(n):
    for j in range(m):
        if mapp[i][j]==2:
            sx, sy =i, j
            break

answer[sx][sy] = 0

q.append((sx, sy, 0))

check =[[False for _ in range(m)] for _ in range(n)]
check[sx][sy] = True

def check_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False


while q:
    cx, cy, cd = q.popleft()

    answer[cx][cy] = cd
    
    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]

        if check_range(nx, ny) and not check[nx][ny] and mapp[nx][ny]==1:
            check[nx][ny] =True
            q.append((nx, ny, cd+1))
    



for i in range(n):
    for j in range(m):
        if mapp[i][j]==0 and answer[i][j]==0:
            print(0, end=" ")
        elif mapp[i][j]==1 and answer[i][j]==0:
            print(-1, end=" ")
        else:
            print(answer[i][j], end=" ")
    print("")