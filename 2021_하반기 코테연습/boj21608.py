n = int(input())

like = [[] for _ in range(n**2+1)]
student = []
for _ in range(n**2):

    tmp = list(map(int, input().split()))

    student.append(tmp[0])

    for i in range(1, len(tmp)):
        like[tmp[0]].append(tmp[i])

mapp = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False

def rule1(cur):
    global mapp
    like_cnt = 0
    space= []

    for i in range(n):
        for j in range(n):
            if mapp[i][j]==0:
                tmp = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if check_range(nx, ny):
                        if mapp[nx][ny] in like[cur]:
                            tmp+=1
                
                if tmp>like_cnt:
                    like_cnt = tmp
                    space = []
                    space.append((i, j))
                elif tmp==like_cnt:
                    space.append((i, j))


    return space



def rule2(cur, space):

    next_space = []
    empty_cnt = 0

    for s in space:
        i, j = s
        tmp = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if check_range(nx,ny) and mapp[nx][ny]==0:
                tmp+=1
        
        if tmp>empty_cnt:
            empty_cnt = tmp
            next_space = []
            next_space.append((i,j))

        elif tmp==empty_cnt:
            next_space.append((i, j))


    return next_space

def calLike():

    answer = 0

    for i in range(n):
        for j in range(n):
            cur_cnt = 0
            cur = mapp[i][j]
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]

                if check_range(nx, ny) and mapp[nx][ny] in like[cur]:
                    cur_cnt+=1

            if cur_cnt==1:
                answer+=1

            elif cur_cnt==2:
                answer+=10
            elif cur_cnt==3:
                answer+=100
            elif cur_cnt==4:
                answer+=1000

    return answer

for curstudent in student:

    space = rule1(curstudent)
    # print(space)
    if len(space)>1:
        space = rule2(curstudent, space)
        
        x, y = space[0]

        mapp[x][y] = curstudent

    else:
        x, y = space[0]
        mapp[x][y] = curstudent
    
    # print("\n")
    # for i in range(n):
    #     for j in range(n):
    #         print(mapp[i][j], end=" ")
    #     print(end="\n")

print(calLike())
    


