answer = 0


def dfs(cur, value,  numList, t, totalSize):

    global answer

    if cur == totalSize:

        if value == t:
            answer += 1
        return

    dfs(cur+1, value-numList[cur],  numList, t, totalSize)

    dfs(cur+1, value+numList[cur],  numList, t, totalSize)


def solution(numbers, target):

    size = len(numbers)

    dfs(0, 0,  numbers, target, size)

    return answer
