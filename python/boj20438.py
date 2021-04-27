import sys
n, k, q, m = map(int, input().split())


sleep = list(map(int, input().split()))

received = list(map(int, input().split()))

check = [1 for _ in range(n+3)]

check[0], check[1], check[2] = 0, 0, 0

for re in received:
    if re not in sleep:
        for j in range(re, n+3, re):
            if j not in sleep:
                check[j] = 0


acc_check = [check[0]]

for i in range(1, len(check)):
    acc_check.append(acc_check[-1]+ check[i])

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    
    answer = acc_check[e]-acc_check[s-1]
    print(answer)




