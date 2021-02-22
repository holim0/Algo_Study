from collections import deque
N, M = map(int, input().split())

answer = []
map_arr = [[] for _ in range(N+1)]

for _ in range(M):
    j, i = map(int, input().split())
    map_arr[i].append(j)


def bfs(start, map_arr, check):

    q = deque([start])
    check[start] = True
    cnt = 0
    while q:
        cur = q.popleft()
        cnt += 1
        size = len(map_arr[cur])
        for i in range(size):
            value = map_arr[cur][i]
            if not check[value]:
                check[value] = True
                q.append((value))

    answer.append((start, cnt))


if __name__ == "__main__":

    for i in range(N):
        check = [False for _ in range(N + 1)]
        bfs(i+1, map_arr, check)


sort_answer = sorted(answer, key=lambda x: -x[1])

tmp = sort_answer[0][1]
real_answer = []
for node, cnt in sort_answer:
    if tmp == cnt:
        real_answer.append(node)

real_answer.sort()

for i in real_answer:
    print(i, end=" ")
