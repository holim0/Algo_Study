n = int(input())
m = int(input())

sosu = [True for _ in range(10005)]

sosu[1] = False

for i in range(2, 100):
    if sosu[i] == True:
        for j in range(i+i, 10001, i):
            sosu[j] = False

min_answer = 0
sum = 0

for i in range(n, m+1):
    if sosu[i]:
        min_answer = i
        break

for i in range(n, m+1):
    if sosu[i]:
        sum += i

if min_answer == 0 and sum == 0:
    print(-1)
else:
    print(sum)
    print(min_answer)
