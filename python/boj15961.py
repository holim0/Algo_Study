from collections import deque
import sys
from typing import Tuple

n, d, k, c = map(int, sys.stdin.readline().split())

sushi= []


for i in range(n):

    tmp = int(sys.stdin.readline())

    sushi.append(tmp)





answer =-1

cur =  deque([])
cnt = 0

visit = [0 for _ in range(3005)]

for i in range(k):
    now = sushi[i]
    
    if visit[now]==0:
        visit[now]= 1
        cnt+=1
    else:
        visit[now]+=1

    cur.append(sushi[i])

if c in cur:
    answer =max(answer, cnt)
else:
    answer = max(answer, cnt+1)


for i in range(1, n):

    removed =cur.popleft()
    
    visit[removed]-=1
    if visit[removed]==0:
        cnt-=1
    
    target = sushi[(i+k-1)%n]
    if  visit[target]==0:
        visit[target]=1
        cnt+=1
    else:
        visit[target]+=1
    cur.append(sushi[(i+k-1)%n])


    if visit[c]!=0:
        answer =max(answer, cnt)
    else:
        answer = max(answer, cnt+1)


print(answer)