from collections import deque



n,m = map(int, input().split())

target = list(map(int, input().split()))

number = [i for i in range(1, n+1)]

q = deque(number)

answer = 0
for a in target:

    while True:
        cur = q[0]
        
        if cur==a:
            
            q.popleft()
            break
        else:
            
            idx = -1
            for i in range(len(q)):
                if q[i]==a:
                    idx = i
                    break
            
            front_d = idx
            back_d = len(q)-idx
            
            if front_d<back_d:
                while True:
                    if q[0]==a: break
                    tmp = q.popleft()
                    q.append(tmp)
                answer+=front_d
            else:
                while True:
                    if q[0]==a: break
                    tmp = q.pop()
                    q.insert(0, tmp)

                answer+=back_d


print(answer)