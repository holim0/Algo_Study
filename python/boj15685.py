import math
n = int(input())

dragon = []

answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

check = [[False] * 102 for _ in range(102)]

dist_dict = {
    0: [1, 0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1]
}

change = {
    0: 1,
    1: 2,
    2: 3,
    3: 0,
}

for i in range(n):
    tmp = list(map(int, input().split()))
    dragon.append(tmp)


def check_box(x, y):
    if check[x][y] and check[x+1][y] and check[x+1][y+1] and check[x][y+1]:
        return True

    return False


def get_dragon(x, y, d, g):
    check[x][y] = True
    check[x+dist_dict[d][0]][y+dist_dict[d][1]] = True

    if g == 0:
        return

    pos = [(x, y), (x+dist_dict[d][0], y + dist_dict[d][1])]

    dir = [d, ]

    for i in range(1, g+1):
        size = len(pos)
        reverse_dir = dir[::-1]
        for j in range(size-1):
            x, y = pos[-1]
            change_dir = change[reverse_dir[j]]
            nx, ny = x+dist_dict[change_dir][0], y+dist_dict[change_dir][1]
            check[nx][ny] = True
            pos.append((nx, ny))
            dir.append(change_dir)


for i in range(n):
    x, y, d, g = dragon[i]
    get_dragon(x, y, d, g)


for i in range(101):
    for j in range(101):
        if check_box(i, j):
            answer += 1

print(answer)
