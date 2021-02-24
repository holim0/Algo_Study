import sys
from collections import deque
t = int(input())

sosu = [True for _ in range(10000)]

for i in range(2, 100):
    if sosu[i] == True:
        for j in range(i+i, 10000, i):
            sosu[j] = False


while t:

    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        print(0)
        t -= 1
        continue

    check = [False for _ in range(10001)]
    q = deque([(a, 0)])

    check[a] = True
    flag = False

    while q:
        cur, answer = q.popleft()
        cur = str(cur)
        if int(cur) == b:
            flag = True
            print(answer)
            break

        for i in range(4):
            tmp = cur
            for j in range(0, 10):
                new = int(tmp[:i]+str(j)+tmp[i+1:])

                if not check[new] and sosu[new] and new >= 1000:
                    check[new] = True
                    q.append((new, answer+1))

    if not flag:
        print("Impossible")

    t -= 1
