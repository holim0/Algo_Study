import sys

n = int(input())

a, b, c, d = [], [], [], []

dict = {}

for i in range(n):
    x, y, z, e = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(e)

answer=0

for i in range(len(a)):
    for j in range(len(b)):
        cur = a[i]+b[j]
        
        if cur not in dict:
            dict[cur] = 1
        
        else:
            dict[cur]+=1


for i in range(len(c)):
    for j in range(len(d)):
        cur = (c[i]+d[j]) * (-1)
        if cur in dict:
            answer+=dict[cur]


    
print(answer)
    