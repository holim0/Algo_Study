from collections import deque
t = int(input())


def bfs(sx, sy, tx, ty, beer):

    q = deque([(sx, sy)])
    check = [False for _ in range(len(beer))]

    while q:
        cx, cy = q.popleft()
        if cx == tx and cy == ty:
            return True

        for i in range(len(beer)):
            x = beer[i][0]
            y = beer[i][1]
            if abs(cx-x)+abs(cy-y) <= 1000 and not check[i]:
                check[i] = True
                q.append((x, y))

    return False


while t:

    n = int(input())

    start = list(map(int, input().split()))

    beer = []

    for i in range(n):
        tmp = list(map(int, input().split()))
        beer.append(tmp)

    festival = list(map(int, input().split()))
    beer.append(festival)

    if bfs(start[0], start[1], festival[0], festival[1], beer):
        print("happy")
    else:
        print("sad")

    t -= 1
