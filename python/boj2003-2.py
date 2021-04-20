n, m  = map(int, input().split())

l = list(map(int, input().split()))

acc = [l[0],]

answer =0

for i in range(1, len(l)):
    acc.append(acc[-1]+l[i])

s, e = 0, 0

while s<len(acc) and e<len(acc):

    sum_val =0

    if s==0:
        sum_val = acc[e]
    else:
        sum_val = acc[e]-acc[s-1]

    
    if sum_val == m:
        answer+=1
        e+=1
        continue

    if sum_val<m:
        e+=1

    elif sum_val>m:
        s+=1



print(answer)    
    