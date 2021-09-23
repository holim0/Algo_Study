from itertools import combinations

h, w = map(int, input().split())
n = int(input())

sti = []

for _ in range(n):
    r, c = map(int, input().split())
    if (r<=h and c<=w) or (r<=w and c<=h):
        sti.append((r, c))

answer = -1


johab = list(combinations(sti, 2))


for cur in johab:
    r1,c1, r2, c2 = cur[0][0], cur[0][1], cur[1][0], cur[1][1]

    rest_r, rest_c = h-r1, w-c1
    rest_r2, rest_c2 = h-c1, w-r1
    
    if rest_r>=0 and rest_c>=0:
       
        if (r2<=rest_r and c2<=w) or (r2<=h and c2<=rest_c):
            answer = max(answer, r1*c1+r2*c2)
        elif (c2<=rest_r and r2<=w) or (c2<=h and r2<=rest_c):
            answer = max(answer, r1*c1+r2*c2)
    
    if rest_r2>=0 and rest_c2>=0:
        if (r2<=rest_r2 and c2<=w) or (r2<=h and c2<=rest_c2):
            answer = max(answer, r1*c1+r2*c2)
        elif (c2<=rest_r2 and r2<=w) or (c2<=h and r2<=rest_c2):
            answer = max(answer, r1*c1+r2*c2)


if answer == -1:
    print(0)
else: 
    print(answer)