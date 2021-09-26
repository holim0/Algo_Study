from collections import deque
import sys

n, m = map(int, input().split())

mapp =[]

iuput = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    tmp = input()
    tmp = list(tmp)
    tmp_list =[]
    for t in tmp:
        tmp_list.append(int(t))
    mapp.append(tmp_list)

def check_range(x, y):
    global n, m 

    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False

INF = 1e10

q = deque([(0, 0, 0)]) ## x, y, cnt

visit = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

visit[0][0][0] = 1

answer = 1e10

while q:
    cx, cy, isbreak = q.popleft()


    if cx==n-1 and cy==m-1:
        answer = visit[n-1][m-1][isbreak]
        break
        

    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]

        if check_range(nx, ny):
            if mapp[nx][ny] ==1 and isbreak==0:
                visit[nx][ny][isbreak+1] = visit[cx][cy][isbreak] +1
                q.append((nx, ny, isbreak+1))


            elif mapp[nx][ny]==0 and not visit[nx][ny][isbreak]:
                visit[nx][ny][isbreak] = visit[cx][cy][isbreak]+1
                q.append((nx, ny, isbreak))

        

if answer == 1e10:
    print(-1)
else:
    print(answer)



