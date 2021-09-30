from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())

dx =[1, -1, 0, 0]

dy =[0, 0, -1, 1]

dh = [1, -1]

def check_done(mapp):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if mapp[i][j][k]==0:
                    return False
    
    return True


def check_range(h, x, y):

    if x>=0 and x<N and y>=0 and y<M and h>=0 and h<H:
        return True
    return False


mapp=[]

check = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for _ in range(H):
    arr= []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
    mapp.append(arr)

if check_done(mapp):
    print(0)
    exit(0)


tomato = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if mapp[i][j][k] ==1:
                check[i][j][k] = True
                tomato.append((i, j, k))



day=0


while tomato:

    if check_done(mapp):
        
        break

    size= len(tomato)
    
    

    for _ in range(len(tomato)):
        h, x, y = tomato.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if check_range(h, nx, ny) and not check[h][nx][ny] and mapp[h][nx][ny]==0:
                mapp[h][nx][ny] = 1
                check[h][nx][ny] = True
                tomato.append((h, nx, ny))

        for k in range(2):
            nh = h+dh[k]

            if check_range(nh, x, y) and not check[nh][x][y] and mapp[nh][x][y]==0:
                mapp[nh][x][y] =1
                check[nh][x][y] = True
                tomato.append((nh, x, y))

    day+=1

if check_done(mapp):
    print(day)
else:
    print(-1)
        
        


