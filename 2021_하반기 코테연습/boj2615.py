mapp = []

isDone = False

for _ in range(19):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

answer_xy = None

def check_range(x, y):
    if x>=0 and x<19 and y>=0 and y<19:
        return True
    return False

def check_back(x, y, factor_x, factor_y, who):
    nx = x+(-factor_x)
    ny = y+(-factor_y)
    if check_range(nx, ny):
        if mapp[nx][ny]==who:
            return False
    
    return True

def getSol(x, y, who):
    global answer_xy
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]


    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]

        if not check_back(x, y, dx[i], dy[i], who): continue

        cnt=1
        answer = [(x, y)]
        if check_range(nx, ny):
            
            while check_range(nx, ny) and mapp[nx][ny]==who:
                cnt+=1
                answer.append((nx, ny))
                
                nx = nx+dx[i]
                ny = ny+dy[i]

            
            if cnt==5:
                
                answer.sort(key=lambda x: (x[1], x[0]))
                answer_xy = answer[0]
                return True
    

    return False




for i in range(19):
    for j in range(19):
        if mapp[i][j]==1:
            if getSol(i, j, 1):
                print(1)
                print(answer_xy[0]+1, answer_xy[1]+1)
                isDone =True
                break


        elif mapp[i][j]==2:
            if getSol(i, j, 2):
                print(2)
                print(answer_xy[0]+1, answer_xy[1]+1)
                isDone =True
                break
    
    if isDone: break
        

if not isDone:
    print(0)

