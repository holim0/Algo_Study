n, x = map(int, input().split())

visit = list(map(int, input().split()))






s = sum(visit[:x])
max_val = sum(visit[:x])
answer = 1

for i in range(1, len(visit)-x+1):
    s-=visit[i-1]
    s+=visit[i+x-1]

    if s>max_val:
        max_val = s
        answer = 1

    elif s==max_val:
        answer+=1

if max_val ==0:
    print("SAD")
else:
    print(max_val)
    print(answer)

