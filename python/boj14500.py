n, m = map(int, input().split())

mapp = []

check = [[False for _ in range(m)] for _ in range(n)]

answer = -1


for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y):
    global n, m
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False



def getSol(cnt, x, y, value):
    global dx, dy, answer
    
    if cnt==3:
        answer = max(answer, value)
    
    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny):
                if check[nx][ny]==False:
                    check[nx][ny] = True
                    getSol(cnt+1, nx, ny, value+mapp[nx][ny])
                    check[nx][ny] = False




for i in range(n):
    for j in range(m):
        check[i][j] = True
        getSol(0, i, j, mapp[i][j])
        check[i][j] = False


for i in range(n):
    for j in range(m):

        if check_range(i+1, j) and check_range(i+1, j+1) and check_range(i+2, j):
            tmp = mapp[i][j] + mapp[i+1][j] + mapp[i+1][j+1] + mapp[i+2][j]
            answer = max(answer, tmp)

        if check_range(i+1, j) and check_range(i+1, j-1) and check_range(i+2, j):
            tmp = mapp[i][j] + mapp[i+1][j] + mapp[i+1][j-1] + mapp[i+2][j]
            answer = max(answer, tmp)
        
        if check_range(i, j+1) and check_range(i, j+2) and check_range(i-1, j+1):
            tmp = mapp[i][j] + mapp[i][j+1] + mapp[i][j+2] + mapp[i-1][j+1]
            answer = max(answer, tmp)

        if check_range(i, j+1) and check_range(i, j+2) and check_range(i+1, j+1):
            tmp = mapp[i][j] + mapp[i][j+1] + mapp[i][j+2] + mapp[i+1][j+1]
            answer = max(answer, tmp)
     

print(answer)