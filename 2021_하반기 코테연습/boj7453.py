from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())

a, b, c, d = [], [], [], []


for i in range(n):
    tmp =list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])


ab_dict = {}



for i in range(n):
    for j in range(n):
        sum_val = a[i]+b[j]
        if sum_val not in ab_dict:
            ab_dict[sum_val]=1
        else:
            ab_dict[sum_val]+=1

answer = 0

for i in range(n):
    for j in range(n):
        sum_val = c[i]+d[j]
        m_sum_val = (-1) * sum_val
        if m_sum_val in ab_dict and ab_dict[-sum_val]!=0:
            answer+=ab_dict[-sum_val]
        




print(answer)