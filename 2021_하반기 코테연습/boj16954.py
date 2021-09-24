from collections import deque

mapp = [[] for _ in range(8)]

wall =[]

dx = [0, 1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, -1, 1, 1, -1, 1, -1]   

for i in range(8):
    tmp = input()
    for j in range(len(tmp)):
        if tmp[j]=="#":
            wall.append((i, j))


def isWall(x, y):

    target = (x,y)

    if target in wall:
        return True

    return False

def check_range(x, y):
    
    if x>=0 and x<8 and y>=0 and y<8:
        return True

    return False





def moveWall():
    global wall

    new_wall = []
    for w in wall:
        x, y = w[0], w[1]
        nx, ny = x+1, y
        if nx<8:
            new_wall.append((nx, ny))
    
    return new_wall

visit = [[[False for _ in range(100)] for _ in range(100)] for _ in range(100)]

q = deque([(7, 0, 0)])

flag =False

visit[7][0][0] = True
time = 0
while q:
    
    for i in range(len(q)):
        cx, cy, cur_time = q.popleft()
        if (cx, cy) in wall:
            continue
        
        if cx==0 and cy==7:
            flag = True
            break

        for i in range(9):
            nx, ny = cx+dx[i], cy+dy[i]

            if check_range(nx, ny) and not visit[nx][ny][cur_time+1] and not isWall(nx, ny):
                visit[nx][ny][cur_time+1] = True
                q.append((nx, ny, cur_time+1))

    if flag == True:
        break
    wall = moveWall()
    



if flag:
    print(1)
else:
    print(0)