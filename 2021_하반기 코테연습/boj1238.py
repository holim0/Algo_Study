import heapq as hp

n, m, x = map(int, input().split())

INF = 1e10

link = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    link[a].append((b, w))


answer = 0

for i in range(1, n+1):
    curStudent = i ## 현재 학생

    dist = [INF for _ in range(n+1)]
    tmp = 0
    dist[curStudent] = 0

    q = []

    hp.heappush(q, (0, curStudent))

    while q:
        w, cur = hp.heappop(q)

        if dist[cur] < w: continue

        for nxt in link[cur]:
            n_node, n_d = nxt
            nxt_dist = n_d+w

            if dist[n_node]> nxt_dist:
                dist[n_node] = nxt_dist
                hp.heappush(q, (nxt_dist, n_node))
    
    tmp+=dist[x]

    dist = [INF for _ in range(n+1)]

    dist[x] = 0

    hp.heappush(q, (0, x))

    while q:
        w, cur = hp.heappop(q)

        if dist[cur] < w: continue

        for nxt in link[cur]:
            n_node, n_d = nxt
            nxt_dist = n_d+w

            if dist[n_node]> nxt_dist:
                dist[n_node] = nxt_dist
                hp.heappush(q, (nxt_dist, n_node))

    tmp+=dist[curStudent]

    answer = max(answer, tmp)


print(answer)