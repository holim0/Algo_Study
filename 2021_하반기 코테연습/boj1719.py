import heapq as hp
n, m = map(int, input().split())

INF = 1e10

link = [[INF for _ in range(n+1)] for _ in range(n+1)]

answer = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    link[a][b] = w
    link[b][a] = w
    answer[a][b] = b
    answer[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if link[i][j]> link[i][k] + link[k][j]:
                link[i][j] = link[i][k] + link[k][j]
                answer[i][j] = answer[i][k]


    

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            print("-", end=" ")

        else:
            print(answer[i][j], end=" ")

    print("")