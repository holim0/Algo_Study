from itertools import combinations

n, m = map(int, input().split())

INF = 1e10
link = [[INF for _ in range(n+1)] for _ in range(n+1)]


number = [i for i in range(1, n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    link[a][b]=1
    link[b][a]=1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            link[i][j] = min(link[i][j], link[i][k]+link[k][j])

johab = list(combinations(number, 2))

check = [False for _ in range(n+1)]
ax, ay, av = -1, -1, 1e10

for j in johab:
    x, y = j
    check[x], check[y]=True, True
    val =0
    for i in range(1, n+1):
        if not check[i]:
            tmp = min(link[i][x], link[i][y])
            val+=tmp

    check[x], check[y]= False, False
        
    if val<av:
        av=val
        ax, ay = x, y

print(ax, ay, av*2)




