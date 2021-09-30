n, m = map(int, input().split())

link = []
INF = 1e10

dist = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c =map(int, input().split())
    link.append((a, b, c))

def getSol(start):

    dist[start] = 0

    for i in range(n+1):
        for j in range(m):
            cur, to, w = link[j]
            if dist[cur]!=INF and dist[cur]+w <dist[to]:
                dist[to] = dist[cur]+w

                if i==n:
                    return False

    return True


if not getSol(1):
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i]==1e10:
            print(-1)
        else:
            print(dist[i])

        