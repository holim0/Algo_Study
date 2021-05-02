import sys
n, m = map(int, input().split())

number = list(map(int, input().split()))
acc = [number[0]]

for i in range(1, len(number)):
    acc.append(acc[-1]+number[i])
    

while m>0:

    s, e = map(int, sys.stdin.readline().split())
    answer = -1
    if s==1:
        answer = acc[e-1]

    else:
        answer= acc[e-1]-acc[s-2]

    print(answer)



    m-=1