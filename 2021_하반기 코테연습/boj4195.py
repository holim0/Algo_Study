import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
parent = None

child_cnt = None

def find(x):

    if x == parent[x]:
        return x

    p = find(parent[x])
    parent[x] = p
    return p

def merge(x, y):
    global parent

    x = find(x)
    y = find(y)

    if x==y: return child_cnt[x]
    

    cnt = child_cnt[x] + child_cnt[y]
    
    if x<y:
        parent[y] = x
        child_cnt[x]+=child_cnt[y]

    else:
        parent[x] = y
        child_cnt[y]+=child_cnt[x]

    return cnt


while t:


    f = int(input())

    parent = {}
    child_cnt = defaultdict(int)

    idx = 0
    for _ in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
        
        if b not in parent:
            parent[b] = b

        if child_cnt[a]==0:
            child_cnt[a]=1
        
        if child_cnt[b]==0:
            child_cnt[b]=1
        answer = merge(a, b)

        print(answer)
        
        
    t-=1