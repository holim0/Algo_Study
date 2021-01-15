from queue import Queue


def solution(n, computers):

    check = [False for _ in range(n)]
    answer = 0
    q = Queue()

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and check[j] == False:
                answer += 1
                q.put(j)
                check[j] = True
                while q.empty() != True:
                    cur = q.get()
                    for k in range(n):
                        if computers[cur][k] == 1 and check[k] == False:
                            print(k)
                            check[k] = True
                            q.put(k)

    return answer
