from collections import deque
import sys
input = sys.stdin.readline

q= deque([])


n = int(input())

for _ in range(n):

    cur = input()
    cur = cur.rstrip("\n")
    cur = cur.split(" ")
    
    if cur[0]=="push":
        cur[1] = cur[1].rstrip("\n")
        q.append(int(cur[1]))

    elif cur[0]=="pop":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())

    elif cur[0]=="size":
        print(len(q))

    elif cur[0]=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)

    elif cur[0]=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])


    elif cur[0]=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])