import copy
from collections import deque
n, m = map(int, input().split())

time =0
cnt=0

cheeze = []


dx = [0, 0, -1, 1]

dy = [-1, 1, 0, 0]


for i in range(n):
    tmp =list(map(int, input().split()))
    cheeze.append(tmp)


def check_range(x, y):

    if x>=0 and x<n and y>=0 and y<m:
        return True
    
    return False


def check_done(map_arr):
    for i in range(n):
        for j in range(m):
            if map_arr[i][j]==1:
                return False

    return True    




while not check_done(cheeze):
    
    air_check = [[False for _ in range(m)] for _ in range(n)]

    q= deque([])

    air_check[0][0]=True

    q.append((0, 0))

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if check_range(nx, ny) and cheeze[nx][ny]==0 and not air_check[nx][ny]:
                air_check[nx][ny] = True
                q.append((nx, ny))

    
    
    time+=1
    gone = []
    original = copy.deepcopy(cheeze)
    for i in range(n):
        for j in range(m):
            if cheeze[i][j]==1:
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if check_range(nx, ny) and air_check[nx][ny]:
                        gone.append((i, j))
                        break
                        
                    
                        
    
    for g in gone:
        x, y = g
        cheeze[x][y]= 0
        

    
    if check_done(cheeze):
        for i in range(n):
            for j in range(m):
                if original[i][j]==1:
                    cnt+=1
        

    
print(time)
print(cnt)

