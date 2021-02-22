import sys
from collections import deque


k = int(input())


while k:

    v, e = map(int, sys.stdin.readline().split())
    m = [[] for _ in range(v+1)]
    check = [False for _ in range(v+1)]

    for _ in range(e):
        i, j = map(int, input().split())
        m[i].append(j)
        m[j].append(i)

    q = deque([])
    marker = [0 for _ in range(v+1)]

    marker[1] = 0

    for i in range(1, v+1):
        if not check[i]:
            check[i] = True
            q.append(i)
            while q:
                cur = q.popleft()
                for i in range(len(m[cur])):
                    val = m[cur][i]
                    if not check[val]:
                        check[val] = True
                        if marker[cur] == 1:
                            marker[val] = 0
                        else:
                            marker[val] = 1

                        q.append(val)

    isYes = True
    for i in range(1, v+1):
        for j in range(len(m[i])):
            val = m[i][j]
            if marker[i] == marker[val]:
                isYes = False
                break

    if isYes:
        print("YES")
    else:
        print("NO")

    k -= 1
