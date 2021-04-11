import sys
from collections import deque

n = int(input())

apple = int(input())

is_apple = [[False for _ in range(n)] for _ in range(n)]

direction = {}

cur_time = 0
cur_dir = "R"
snake = deque([(0,0)])

dir_mapping ={
    "UL" : "L",
    "UR" : "R",
    "DL" : "R",
    "DR" : "L",
    "LL": "D",
    "LR" : "U",
    "RL" : "U",
    "RR" :  "D"
}

dir_value = {
    "U": [-1, 0],
    "D" : [1, 0],
    "L": [0, -1],
    "R": [0, 1],
}

for i in range(apple):
    x, y  = map(int, sys.stdin.readline().split())
    is_apple[x-1][y-1] = True


L = int(input())

for i in range(L):
    time, d = sys.stdin.readline().split()
    time = int(time)
    if d =="D" :
        direction[time] = "R"
    else:
        direction[time] = "L"

def check_Done(headx, heady):
    global cur_time, snake
    if (headx, heady) in snake and len(snake)>1:
        return True

    if headx<0 or headx>=n or heady<0 or heady>=n:
        return True
    
    
    return False
    
    
curheadx, curheady = 0, 0


while True:

    cur_time+=1

    
    
    # print(cur_time, cur_dir, curheadx, curheady, "뱀길이:", len(snake), snake)

    next_Head_x, next_Head_y  =  curheadx+dir_value[cur_dir][0], curheady+dir_value[cur_dir][1]

    if check_Done(next_Head_x, next_Head_y):
        break


    if is_apple[next_Head_x][next_Head_y]:
        snake.append((next_Head_x, next_Head_y))
        is_apple[next_Head_x][next_Head_y]=False
    
    else:
        snake.popleft()
        snake.append((next_Head_x, next_Head_y))
    
    

    if cur_time in direction:
        next_dir = cur_dir+ direction[cur_time]
        next_dir = dir_mapping[next_dir]
        cur_dir = next_dir

    curheadx, curheady = next_Head_x, next_Head_y



print(cur_time)



