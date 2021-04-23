import math
n = int(input())

if n == 1:
    print(0)
    exit(0)
sosu = [True for _ in range(n+1)]

real_sosu = []
upper = int(math.sqrt(n+1))+1


for i in range(2, upper):
    if sosu[i]:
        for j in range(i+i, n+1, i):
            sosu[j]= False

for i in range(2, len(sosu)):
    if sosu[i]:
        real_sosu.append(i)

acc_sosu = [real_sosu[0]]

for i in range(1, len(real_sosu)):
    acc_sosu.append(acc_sosu[-1]+ real_sosu[i])

s, e = 0, 0 
answer =0

while s<len(acc_sosu) and e<len(acc_sosu):

    cur = 0

    if s==0:
        cur = acc_sosu[e]
    
    else:
        cur = acc_sosu[e]- acc_sosu[s-1]
    

    if cur==n :
        answer+=1
        e+=1
    
    elif cur<n:
        e+=1
    
    elif cur>n:
        s+=1


print(answer)


