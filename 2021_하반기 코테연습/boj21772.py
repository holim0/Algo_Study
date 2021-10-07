import sys
input = sys.stdin.readline


r, c, t = map(int, input().split())

mapp = []


sx, sy = -1, -1


for _ in range(r):
    tmp = input()
    tmp = list(tmp)
    mapp.append(tmp)

for i in range(r):
    for j in range(c):
        if mapp[i][j]=="G":
            sx, sy = i, j
            break


dx= [1, -1, 0, 0]
dy = [0, 0, -1, 1]


visit = [[[False for _ in range(c)] for _ in range(r)] for _ in range(t+1)]

answer = 0




def check_range(x, y):
    if x>=0 and x<r and y>=0 and y<c:
        return True
    return False

def move(x,y, cur_time, gogu):
    global answer

    if cur_time>t: return 
    if cur_time==t:
        answer = max(answer, gogu)
        return

    

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if check_range(nx, ny) and mapp[nx][ny]!="#":
            
            if not visit[cur_time+1][nx][ny]:
                visit[cur_time+1][nx][ny] = True
                
                if mapp[nx][ny]=="S":
                    mapp[nx][ny]="."
                    move(nx, ny, cur_time+1, gogu+1)
                    mapp[nx][ny]="S"
                else:
                    move(nx, ny, cur_time+1, gogu)
                
                visit[cur_time+1][nx][ny] = False



visit[0][sx][sy] = True
move(sx, sy, 0, 0)

print(answer)
