n = int(input())


cnt = 0

check = [-1 for _ in range(n+1)]

for _ in range(n):
    number, d= map(int, input().split())

    if check[number]==-1:
        check[number]=d
    
    else:
        if check[number]!=d:
            cnt+=1
            check[number]=d

print(cnt)