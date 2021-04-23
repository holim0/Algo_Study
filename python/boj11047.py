n, k = map(int, input().split())

money = []

answer=0

for i in range(n):
    m =int(input())
    money.append(m)

money.sort(reverse=True)

for m in money:
    
    if m<=k:
        answer+=k//m
        k= k%m
    

print(answer)

