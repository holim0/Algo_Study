from collections import defaultdict
t = int(input())

parent = defaultdict(str)


def find(x):

    if parent[x]==x:
        return x
    
    p = parent[x]
    parent[x] = p
    return p

def merge(x, y):
    
    x = find(x)
    y = find(y)

    if x==y: return 

    parent[x] = y


while t:

    f = int(input())

    




    t-=1