n = int(input())

INF = 1e10

link = [[INF for _ in range(60)] for _ in range(60)]

answer= []
for _ in range(n):
    command = input()

    command = command.split(" => ")
    a, b = ord(command[0])-65, ord(command[1])-65


    link[a][b]=1


for k in range(60):
    for i in range(60):
        for j in range(60):
            link[i][j] = min(link[i][j], link[i][k]+link[k][j])

for i in range(60):
    for j in range(60):

        if link[i][j] != INF:
            a, b = chr(i+65), chr(j+65)
            if a!=b:
                answer.append((a, b))

answer.sort(key = lambda x: (x[0], x[1]))
print(len(answer))

for a in answer:
    if a[0]!=a[1]:
        print("{f} => {to}".format(f=a[0], to=a[1]))





