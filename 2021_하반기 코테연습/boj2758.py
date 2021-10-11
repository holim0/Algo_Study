mapp = []
check = [[False for _ in range(5)] for _ in range(5)]

for _ in range(5):
    tmp = list(map(int,input().split()))
    mapp.append(tmp)

location = {}


def check_done():

    cnt = 0

    for i in range(5):
        if check[i][0] and check[i][1] and check[i][2] and check[i][3] and check[i][4]:
            cnt+=1
        
    for j in range(5):
        if check[0][j] and check[1][j] and check[2][j] and check[3][j] and check[4][j]:
            cnt+=1

    if check[0][0] and check[1][1] and check[2][2] and check[3][3] and check[4][4]:
        cnt+=1

    if check[4][0] and check[3][1] and check[2][2] and check[1][3] and check[0][4]:
        cnt+=1




    if cnt>=3:
        return True
    
    return False



for i in range(5):
    for j in range(5):
        cur = mapp[i][j]
        if cur not in location:
            location[cur] = (i, j)
isDone = False
oper = []
for _ in range(5):
    tmp = list(map(int, input().split()))
    oper.append(tmp)

time = 0
for i in range(5):
    for j in range(5):
        cur = oper[i][j]

        x, y = location[cur]

        check[x][y] = True
        time+=1
        if check_done():
            isDone = True
            break
    
    if isDone: break

        
    


print(time)

