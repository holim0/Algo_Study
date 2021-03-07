import sys
import math
max_val = 10000
t = int(input())


sosu = [True for _ in range(max_val)]

sosu[0], sosu[1] = False, False

for i in range(2, int(math.sqrt(max_val))):
    if sosu[i]:
        for j in range(i+i, max_val, i):
            sosu[j] = False

partition = []

for i in range(t):
    n = int(sys.stdin.readline())
    partition.clear()
    for j in range(2, n):
        if sosu[j]:
            rest = n-j
            if sosu[rest]:
                partition.append((j, rest, abs(j-rest)))

    partition.sort(key=lambda x: x[2])

    a, b, c = partition[0]
    print(a, b)
