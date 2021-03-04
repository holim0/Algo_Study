import sys
from collections import deque
n, m = map(int, input().split())

dict = {}


for i in range(n+m):
    x, y = map(int, sys.stdin.readline().split())
    dict[x] = y


answer = 987654321
start = 1

q = deque([(start, 0)])


visit = [200 for _ in range(101)]


visit[1] = 0

while q:
    cur, cnt = q.popleft()
    if cur == 100:
        answer = min(answer, cnt)
        continue

    else:
        for i in range(1, 7):
            next = cur+i

            if next > 100:
                break

            if next in dict:
                next = dict[next]

            if visit[next] > cnt+1:
                visit[next] = cnt+1
                q.append((next, cnt+1))


print(answer)
