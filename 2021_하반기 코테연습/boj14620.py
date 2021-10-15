n = int(input())

mapp = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

check = [[False for _ in range(n)] for _ in range(n)]

answer = 1e10

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False

def check_find(x, y):
    global dx, dy

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not check_range(nx, ny) or check[nx][ny]:
            return False

    return True

def get_sum(x, y):
    global dx, dy
    s = mapp[x][y]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        s+=mapp[nx][ny]
    return s

def getSol(cur, cnt):
    global answer, dx, dy

    if cnt==3:
        answer = min(answer, cur)
        return

    for i in range(n):
        for j in range(n):
            if not check[i][j] and check_find(i, j):
                tmp= mapp[i][j]

                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    check[nx][ny] = True
                    tmp+=mapp[nx][ny]
                
                getSol(cur+tmp, cnt+1)

                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    check[nx][ny] = False

            
                
getSol(0, 0)                 

        

print(answer)