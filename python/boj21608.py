n = int(input())

school = [[0 for _ in range(n)] for _ in range(n)]


like =[]

answer =0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


dict={}

for i in range(n*n):
    tmp = list(map(int, input().split()))
    like.append(tmp)

    if tmp[0] not in dict:
        dict[tmp[0]] = tmp[1:]



def check_range(x, y):
    
    if x>=0 and x<n and y>=0 and y<n:
        return True
    
    else: 
        return False


def find_loc(target, like_friend):
    global school

    tx, ty =100, 100
    max_like = 0
    max_empty  = 0
    for i in range(n):
        for j in range(n):
            if school[i][j]==0:
                like_cnt=0
                empty_cnt =0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if check_range(nx, ny):

                        if school[nx][ny]==0:
                            empty_cnt+=1
                            continue

                        if school[nx][ny] in like_friend:
                            like_cnt+=1
                            

                        

                if like_cnt==max_like:
                    if empty_cnt>max_empty:
                        max_empty=empty_cnt
                        tx, ty= i, j

                    elif empty_cnt== max_empty:
                        if tx>i:
                            tx, ty =i,j 
                        elif tx==i:
                            if ty>j:
                                tx, ty=i, j

                    
                elif like_cnt>max_like:
                    tx, ty = i, j
                    max_empty= empty_cnt
                    max_like = like_cnt
                        
                
                
                
    
    return (tx, ty)






for i in range(len(like)):
    target =like[i][0]

    x, y = find_loc(target, like[i][1:])
    
    school[x][y] = target
    


for i in range(len(school)):
    for j in range(len(school)):
        cnt = 0
        cur = school[i][j]

        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]

            if check_range(nx, ny):
                if school[nx][ny] in dict[cur]:
                    cnt+=1


        if cnt==1:
            answer+=1

        elif cnt==2:
            answer+=10

        elif cnt==3:
            answer+=100

        elif cnt==4:
            answer+=1000



print(answer)



