import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0 for _ in range(n+1)]

for i in range(1, n+1):
    parent[i] = i


def find(x):

    if parent[x]==x:
        return x


    p = find(parent[x])
    parent[x] = p
    return p

def merge(x, y):
    
    x = find(x)
    y = find(y)

    if x==y: return 

    if x<y:
        parent[y] =x
    else:
        parent[x] = y


for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]==1:
            merge(i+1, j+1)

road = list(map(int, input().split()))

s = set()


for r in road:
    p = find(r)
    s.add(p)

if len(s)==1:
    print("YES")
else:
    print("NO")