import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

namu = []

answer = 0
for _ in range(n):
    tmp =list(map(int, input().split()))
    namu.append(tmp)

if n<2 or m<2:
    print(0)
    exit(0)

dir = [
    [(-1,0), (0, 1)],
    [(-1,0), (0, -1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)]
]

visit = [[False for _ in range(m)] for _ in range(n)]

def check_range(x, y):

    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False




def getSol(x,y, cnt, cur_visit):
    global answer
    if y==m:
        x+=1
        y=0


    if x==n:
        answer = max(answer, cnt)
        return
         

    for d in dir:
        nx1, ny1, nx2, ny2 = x+d[0][0], y+d[0][1], x+d[1][0], y+d[1][1]
        if check_range(nx1, ny1) and check_range(nx2, ny2):
            if not cur_visit[nx1][ny1] and not cur_visit[nx2][ny2] and not cur_visit[x][y]:
                cur_visit[nx1][ny1] = True
                cur_visit[nx2][ny2] = True
                cur_visit[x][y] = True
                next_sum = 2*namu[x][y] + namu[nx1][ny1]+namu[nx2][ny2]
                getSol(x, y+1, cnt+next_sum, cur_visit)
                cur_visit[nx1][ny1] = False
                cur_visit[nx2][ny2] = False
                cur_visit[x][y] = False

    getSol(x, y+1, cnt, cur_visit)
               

    

    

visit = [[False for _ in range(m)] for _ in range(n)]
getSol(0, 0, 0,visit)


print(answer)