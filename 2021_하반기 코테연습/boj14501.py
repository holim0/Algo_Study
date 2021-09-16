from itertools import combinations
from collections import deque
import copy


n, m = map(int, input().split())

mapp = []

answer = -1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, input().split()))

    mapp.append(tmp)


empty = []

for i in range(n):
    for j in range(m):
        if mapp[i][j]==0:
            empty.append((i, j))


empty_j = list(combinations(empty, 3))


def check_range(x, y):
    global n, m

    if x>=0 and x<n and y>=0 and y<m:
        return True
    
    return False


def get_cnt(cur):
    global n, m
    cnt=0
    for i in range(n):
        for j in range(m):
            if cur[i][j]==0:
                cnt+=1

    return cnt


for cur in empty_j:
    (x1, y1), (x2, y2), (x3, y3) = cur
    copy_mapp = copy.deepcopy(mapp)

    copy_mapp[x1][y1] = 1
    copy_mapp[x2][y2] = 1
    copy_mapp[x3][y3] = 1

    visit = [[False for _ in range(m)] for _ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(m):
            if copy_mapp[i][j]==2 and visit[i][j]==False:
                visit[i][j] = True
                q.append((i, j))
                
                while q:
                    cx, cy = q.popleft()

                    for k in range(4):
                        nx, ny = cx+dx[k], cy+dy[k]

                        if check_range(nx, ny) and copy_mapp[nx][ny]==0:
                            copy_mapp[nx][ny]=2
                            visit[nx][ny] = True
                            q.append((nx, ny))

    

    answer =max(answer, get_cnt(copy_mapp))
                



print(answer)

