r, c = map(int, input().split())

gr, gr, br, bc = map(int, input().split())


mapp = []

for i in range(r):
    tmp = input()
    tmp = list(tmp)
    mapp.append(tmp)

cnt = 0


for i in range(r):
    for j in range(c):
        if mapp[i][j]=="P": cnt+=1

if cnt== br*bc:
    print(0)

else:
    print(1)
