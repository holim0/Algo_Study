n = int(input())


arr = [list(map(int, input().split())) for _ in range(n)]

a, b, c, d = list(), list(), list(), list()

for i in range(n):
    for j in range(4):
        if j == 0:
            a.append(arr[i][j])

        elif j == 1:
            b.append(arr[i][j])

        elif j == 2:
            c.append(arr[i][j])

        elif j == 3:
            d.append(arr[i][j])


dict = {}

for i in a:
    for j in b:
        dict[i+j] = dict.get(i+j, 0) + 1

answer = 0
for i in c:
    for j in d:
        answer += dict.get(-(i+j), 0)


print(answer)
