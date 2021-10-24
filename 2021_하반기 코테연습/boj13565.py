from collections import deque

n, m = map(int, input().split())

mapp = []

for _ in range(n):
    tmp = input()
    tmp.rstrip("\n")
    tmp = list(tmp)
    mapp.append(tmp)


q =deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

check = [[False for _ in range(m)] for _ in range(n)]

for i in range(m):

    if not check[0][i] and mapp[0][i]=="0":
        check[0][i] = True
        q.append((0, i))


        while q:
            cx, cy = q.popleft()
            
            if cx==n-1:
                print("YES")
                exit(0)


            for k in range(4):
                nx, ny = cx+dx[k], cy+dy[k]

                if nx>=0 and nx<n and ny>=0 and ny<m:
                    if not check[nx][ny] and mapp[nx][ny]=="0":
                        check[nx][ny] = True
                        q.append((nx, ny))


print("NO")