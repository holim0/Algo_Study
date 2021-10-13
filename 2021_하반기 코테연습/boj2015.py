from collections import defaultdict
n, k = map(int, input().split())

number = list(map(int, input().split()))

cnt = defaultdict(int)

acc = [number[0]]


for i in range(1, len(number)):
    acc.append(acc[-1]+number[i])

answer =0

for i in range(len(acc)):
    if acc[i]==k:
        answer+=1
    target = acc[i]-k
    answer+=cnt[target]
    cnt[acc[i]]+=1
print(answer)