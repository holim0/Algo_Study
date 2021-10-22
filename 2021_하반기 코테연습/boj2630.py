from collections import deque

n = int(input())

mapp = []

for _ in range(n):
    tmp =list(map(int, input().split()))
    mapp.append(tmp)

blue_cnt=0
white_cnt = 0


def check_same_paint(cx, cy, cur_size):

    size = cur_size
    blue=0
    white = 0
    for i in range(cx, cx+size):
        for j in range(cy, cy+size):
            if mapp[i][j]==0:
                white+=1
            elif mapp[i][j]==1:
                blue+=1
    
    if blue==0 or white==0: return True
    return False

def what_color(cx, cy):
    global blue_cnt, white_cnt
    if mapp[cx][cy]==1:
        blue_cnt+=1

    else:
        white_cnt+=1
    

def cut(cx, cy, cur_size):

    if check_same_paint(cx, cy, cur_size):
        what_color(cx, cy)
        return 

    else:
        next_size = cur_size//2
        cut(cx, cy, next_size)
        cut(cx, cy+next_size, next_size)
        cut(cx+next_size, cy, next_size)
        cut(cx+next_size, cy+next_size, next_size)
        

cut(0, 0, n)

print(white_cnt)
print(blue_cnt)