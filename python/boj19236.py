import sys
import copy

water = [[] * 4 for _ in range(4)]
answer = 0
dir_mapping = {
    1: (-1, 0),
    2: (-1, -1),
    3:  (0, -1),
    4:  (1, -1),
    5:  (1, 0),
    6:  (1, 1),
    7:  (0, 1),
    8:  (-1, 1)
}

for i in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, len(tmp)-1, 2):
        water[i].append((tmp[j], tmp[j+1]))


def check_done(x, y, curMap):

    for i in range(1, 9):
        fx, fy = dir_mapping[i]
        nx, ny = x+fx, y+fy

        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            fishNum, fishDir = curMap[nx][ny]
            if fishNum != -1 and fishDir != -1:
                return False

    return True


def can_move(x, y, curMap, sharkx, sharky):

    if x >= 0 and x < 4 and y >= 0 and y < 4 and (x != sharkx or y != sharky):
        return True

    return False


def rotate_dir(x, y, sharkx, sharky, dir, curMap):

    new_dir = -1

    for i in range(1, 8):
        dir = (dir+1)

        if dir > 8:
            dir = 1

        nx, ny = x+dir_mapping[dir][0], y+dir_mapping[dir][1]
        if can_move(nx, ny, curMap, sharkx, sharky):
            new_dir = dir
            break

    return new_dir


def moveFish(curMap, sharkx, sharky):

    moveMap = copy.deepcopy(curMap)
    fish = {}
    number = []

    for i in range(4):
        for j in range(4):
            n, dir = moveMap[i][j]
            if n != -1:
                fish[n] = [i, j, dir]
                number.append(n)

    number.sort()

    for cur_number in number:
        curx, cury, curdir = fish[cur_number][0], fish[cur_number][1], fish[cur_number][2]
        nx, ny = curx+dir_mapping[curdir][0], cury+dir_mapping[curdir][1]

        if can_move(nx, ny, moveMap, sharkx, sharky) == False:

            rotated_dir = rotate_dir(
                curx, cury, sharkx, sharky, curdir, moveMap)
            if rotated_dir == -1:
                continue
            curdir = rotated_dir
            nx = curx + dir_mapping[rotated_dir][0]
            ny = cury + dir_mapping[rotated_dir][1]

        target_number, target_dir = moveMap[nx][ny]

        if target_number != -1 and target_dir != -1:

            moveMap[nx][ny] = (cur_number, curdir)
            fish[cur_number] = [nx, ny, curdir]

            moveMap[curx][cury] = (target_number, target_dir)
            fish[target_number] = [curx, cury, target_dir]

        else:

            moveMap[nx][ny] = (cur_number, curdir)
            moveMap[curx][cury] = (-1, -1)
            fish[cur_number] = [nx, ny, curdir]

    return moveMap


def dfs(cx, cy, cnt, curMap):
    global answer
    tmpMap = copy.deepcopy(curMap)

    cost, curdir = tmpMap[cx][cy]

    tmpList = list(tmpMap[cx][cy])
    tmpList[0], tmpList[1] = -1, -1
    tmpMap[cx][cy] = tuple(tmpList)
    cnt += cost

    answer = max(answer, cnt)

    after_move = moveFish(tmpMap, cx, cy)

    for i in range(1, 4):
        nextx, nexty = cx + \
            dir_mapping[curdir][0] * i, cy+dir_mapping[curdir][1] * i

        if nextx >= 0 and nextx < 4 and nexty >= 0 and nexty < 4:
            if after_move[nextx][nexty][0] != -1 and after_move[nextx][nexty][1] != -1:
                dfs(nextx, nexty, cnt, after_move)
        else:
            break

    return


if __name__ == "__main__":
    dfs(0, 0, 0, water)
    print(answer)
