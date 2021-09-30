n = int(input())

number= list(map(int, input().split()))

x = int(input())
number.sort()

s, e = 0, n-1

answer= 0

while s<e and e<n:

    cur = number[s]+number[e]
    
    if cur==x:
        answer+=1
        e-=1

    elif cur>x:
        e-=1

    elif cur<x:
        s+=1


print(answer)