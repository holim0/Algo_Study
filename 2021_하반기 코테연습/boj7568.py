n = int(input())

info = []

for i in range(n):
    a, b = map(int, input().split())

    info.append((a, b, i))




sorted_info = sorted(info, key=lambda x: (-x[0], -x[1]))

answer =[-1 for _ in range(n)]

for i in range(len(sorted_info)):
    cur = sorted_info[i]
    origin_idx = cur[2]
    if i==0:
        answer[origin_idx] = 1
    else:
        cnt = 0
        for j in range(0, i):
            prev = sorted_info[j]
            if cur[0]<prev[0] and cur[1]<prev[1]:
                cnt +=1

        answer[origin_idx] = cnt+1
            

            
                


for i in range(len(answer)):
    print(answer[i], end=" ")

