def check(x, y):
    if x > 5 or x < -5 or y > 5 or y < -5:
        return False

    return True


def list_check(list, way, way2):

    if way not in list and way2 not in list:
        return True
    else:
        return False


def solution(dirs):
    answer = 0

    curx = 0
    cury = 0

    list = []

    for dir in dirs:
        way = ""
        way2 = ""

        if dir == 'U':
            tx = curx+1
            ty = cury

        elif dir == 'D':
            tx = curx-1
            ty = cury

        elif dir == 'R':
            tx = curx
            ty = cury+1

        elif dir == 'L':
            tx = curx
            ty = cury-1

        way = str(curx)+str(cury)+str(tx)+str(ty)
        way2 = str(tx)+str(ty)+str(curx)+str(cury)

        if check(tx, ty) == False:
            continue
        else:
            if list_check(list, way, way2) == True:
                list.append(way)
                list.append(way2)
                answer += 1
            curx = tx
            cury = ty

    return answer
