from collections import deque

n, m = map(int, input().split())

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

maap = []

for i in range(n):

    tmp = list(map(int, input().split()))

    maap.append(tmp)


answer = 0

visit = [[False for _ in range(m)] for _ in range(n)]

q= deque([])

def check_range(x, y):
    global n, m

    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False

for i in range(n):
    for j in range(m):
        cur = maap[i][j]

        if cur ==1 and not visit[i][j]:
            answer+=1
            visit[i][j]= True
            
            q.append((i, j))

            while q:
                cx, cy = q.popleft()

                
                for k in range(8):
                    nx, ny = cx+dx[k], cy+dy[k]

                    if check_range(nx, ny) and maap[nx][ny]==1 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        q.append((nx,ny))


print(answer)

