import sys
input = sys.stdin.readline


n, m = map(int, input().split())


INF = 1e10
answer = 1e10

link = [[INF for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m):
    a, b,c = map(int, input().split())
    link[a][b] = c



for i in range(1, n+1):
    link[i][i]=0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if link[i][j] > link[i][k]+link[k][j]:
                link[i][j] = link[i][k]+link[k][j]

for i in range(1, n+1):
    for j in range(i+1, n+1):
        answer = min(answer, link[i][j]+link[j][i])

if answer == 1e10:
    print(-1)
else:
    print(answer)
