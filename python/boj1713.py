n = int(input())
cnt = int(input())

arr = list(map(int, input().split()))

photo = {}

for i in range(len(arr)):

    cur =arr[i]
    if len(photo)<n:
        if cur not in photo:
            photo[cur] = [1, i]

        else:
            photo[cur][0]+=1

    else:
        if cur in photo:
            photo[cur][0]+=1
        else:
            toList = sorted(photo.items(), key= lambda x: (-x[1][0], -x[1][1]))
            toList.pop()
            toList.append((cur, [1, i]))
            photo = dict(toList)

answer =[]
for key, value in photo.items():
    answer.append(key)

answer.sort()

for a in answer:
    print(a, end=" ")