from collections import deque

n, k = map(int, input().split())

arr = list(map(int, input().split()))

up = deque([])

check_up = deque([-1 for _ in range(n)])

down = deque([])



stage = 1




def check_done():
    global up, down, k
    cnt=0

    for i in range(len(up)):
        if up[i]==0: cnt+=1

    for i in range(len(down)):
        if down[i] == 0: cnt+=1

    
    if cnt>=k: return True

    return False

for i in range(n):
    up.append(arr[i])
    down.append(arr[i+n])

down.reverse()

while True:

    ## 1. 회전 후 내리기 
   
    down.append(up[-1])
    up.pop()

    up.appendleft(down[0])
    down.popleft()

    
    check_up.pop()
    check_up.appendleft(-1)

    check_up[-1]=-1
    

    

    

    
    ## 2. 로봇 무브 


    for i in range(len(check_up)-1, -1, -1):
        cur_idx=i
        if check_up[i] !=-1:
            if cur_idx != len(check_up)-1 and up[cur_idx+1]>0 and check_up[cur_idx+1]==-1:
                check_up[cur_idx+1] = check_up[cur_idx]
                up[cur_idx+1]-=1
                check_up[cur_idx]= -1



            
    
    
    ## 3. 로봇 놓기

    if up[0]>0 :
        check_up[0]=stage
        up[0]-=1
    

    
    if check_done():
        break
    
    stage+=1


print(stage)
