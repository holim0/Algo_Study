n = int(input())
m = int(input())

INF = 1e10

link = [[INF for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    link[a][b] = min(link[a][b], c)


for i in range(1, n+1):
    link[i][i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            link[i][j] = min(link[i][j], link[i][k]+link[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        
        if link[i][j]==INF:
            print(0, end=" ")

        else:
            print(link[i][j], end=" ")

    print(end="\n")