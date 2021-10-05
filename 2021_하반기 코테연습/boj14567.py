from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

link = [[] for _ in range(n+1)]

degree = [0 for _ in range(n+1)]
answer = [-1 for _ in range(n+1)]

cnt = 1

for _ in range(m):

    a, b = map(int, input().split())
    link[a].append(b)
    degree[b]+=1


q = deque([])

for i in range(1, n+1):
    if degree[i]==0:
        q.append((i, 1))


while q:

    size = len(q)

    for _ in range(size):
        cur, day = q.popleft()
        answer[cur]=day
        for nxt in link[cur]:
            degree[nxt]-=1
            
            if degree[nxt]==0:
                q.append((nxt, cnt+1))

    cnt+=1



for i in range(1, n+1):
    print(answer[i], end=" ")