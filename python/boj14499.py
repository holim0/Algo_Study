n, m, x, y, k = map(int, input().split())


mapp = []

for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

command = list(map(int, input().split()))

dir = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

jusa= [[-1, 0, -1],[0, 0, 0], [-1, 0, -1], [-1, 0, -1]]

def check_range(x, y):
    global n, m 

    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def move_jusa(cur_dir):
    global jusa

    if cur_dir ==1:
        tmp = jusa[3][1]
        jusa[3][1] = jusa[1][2]
        jusa[1][2] = jusa[1][1]
        jusa[1][1] = jusa[1][0]
        jusa[1][0] = tmp

    elif cur_dir==2:
        tmp = jusa[3][1]
        jusa[3][1] = jusa[1][0]
        jusa[1][0] = jusa[1][1]
        jusa[1][1] = jusa[1][2]
        jusa[1][2] = tmp
    elif cur_dir==3:
        tmp = jusa[3][1]
        jusa[3][1] = jusa[2][1]
        jusa[2][1] = jusa[1][1]
        jusa[1][1] = jusa[0][1]
        jusa[0][1] = tmp

    elif cur_dir ==4:
        tmp = jusa[0][1]
        jusa[0][1] = jusa[1][1]
        jusa[1][1] = jusa[2][1]
        jusa[2][1] = jusa[3][1]
        jusa[3][1] = tmp




for i in range(len(command)):
    cur_command = command[i]

    next_x, next_y = x+dir[cur_command][0], y+dir[cur_command][1]

    if check_range(next_x, next_y):
        move_jusa(cur_command)
        
        x, y = next_x, next_y

        if mapp[x][y] == 0:
            mapp[x][y] = jusa[3][1]

        else:
            jusa[3][1] = mapp[x][y]
            mapp[x][y]=0    
        
        print(jusa[1][1])
