n, m, r = map(int, input().split())

item = list(map(int, input().split()))

INF = 1e10
link = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    link[i][i] = 0

for _ in range(r):
    a, b, w = map(int, input().split())
    link[a][b] = w
    link[b][a] = w

answer= 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            link[i][j] = min(link[i][j], link[i][k]+link[k][j])

for start in range(1, n+1):
    tmp = 0
    for to in range(1, n+1):
        if link[start][to]<=m:
            tmp+=item[to-1]

    answer = max(answer, tmp)


print(answer)