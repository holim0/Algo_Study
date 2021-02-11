from collections import deque


def solution(n, computers):
    answer = 0

    size = len(computers)

    check = [False for _ in range(size)]
    q = deque([])

    for i in range(size):
        if not check[i]:
            check[i] = True
            answer += 1
            q.append(i)

            while q:
                cur = q.popleft()

                for j in range(size):
                    if computers[cur][j] == 1 and not check[j]:
                        check[j] = True
                        q.append(j)

    return answer
