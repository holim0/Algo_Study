n = int(input())

mapp = []


for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

dist = [[0 for _ in range(n)] for _ in range(n)]

INF = 987654321

for i in range(n):
    for j in range(n):
        if mapp[i][j]==1:
            dist[i][j] = 1

        else:
            dist[i][j]= INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])


answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            answer[i][j]=0
        else:
            answer[i][j]= 1

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print("")
    