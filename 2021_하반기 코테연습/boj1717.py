import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())

parent = [0 for _ in range(n+1)]

for i in range(1, n+1):
    parent[i]= i


def find(x):

    if parent[x]==x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def merge(x, y):

    x = find(x)
    y = find(y)

    if x==y:return

    parent[y] = x

def isSame(x,y):

    x= find(x)
    y= find(y)

    if x==y: return True

    return False


for _ in range(m):
    command, a, b = map(int, input().split())

    if command==0:
        merge(a, b)
    else:
        if isSame(a, b):
            print("YES")
            print("\n")
        else:
            print("NO")
            print("\n")
