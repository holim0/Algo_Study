k, n = map(int, input().split())

number = []
answer = -1

for i in range(k):

    tmp = int(input())

    number.append(tmp)


number.sort()

s, e = 1, number[-1]


while s<=e:

    mid = (s+e)//2
    
    cnt = 0

    for i in range(len(number)):
        cnt+= (number[i]//mid)

    if cnt>=n:
        answer = max(answer, mid)
        s = mid+1
    else:
        e = mid-1


print(answer)