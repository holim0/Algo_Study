h, w = map(int, input().split())

mapp = list(map(int, input().split()))

answer =0
size = len(mapp)
for i in range(1, size-1):
    l_max = max(mapp[:i])
    r_max = max(mapp[i+1:])

    min_val = min(l_max, r_max)

    if min_val>=mapp[i]:
        answer+=min_val-mapp[i]


print(answer)