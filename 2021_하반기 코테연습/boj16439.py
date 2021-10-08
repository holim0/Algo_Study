from itertools import combinations

n, m = map(int, input().split())

chick = [i for i in range(m)]

preper = []
answer = -1
for _ in range(n):
    tmp = list(map(int, input().split()))
    preper.append(tmp)


for i in range(1, 4):
    chickJohab = list(combinations(chick, i))
    
    for j in chickJohab:
        tmp = 0
        for k in range(n):
            ttmp =0
            for jj in j:
                ttmp = max(ttmp, preper[k][jj-1])
            tmp+=ttmp

        answer = max(answer, tmp)




print(answer)

