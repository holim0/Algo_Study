from collections import deque

n, k = map(int, input().split())


q = deque([])

answer =[]

for i in range(1, n+1):
    q.append(i)


while q:

    cnt = 0

    while True:
        cnt+=1
        if cnt==k:
            tmp = q.popleft()
            answer.append(str(tmp))
            break

        tmp = q.popleft()
        q.append(tmp)


answer = ", ".join(answer)

answer = "<"+answer+">"

print(answer)