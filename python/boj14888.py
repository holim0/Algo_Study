import sys

N = int(input())

numberList = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxAnswer = -1000000000
minAnswer = 1000000000


def dfs(idx, s, plus, minus, mul, div):
    global numberList, maxAnswer, minAnswer
    if plus == 0 and minus == 0 and mul == 0 and div == 0:

        maxAnswer = max(maxAnswer, s)
        minAnswer = min(minAnswer, s)
        return

    if plus > 0:
        dfs(idx+1, s+numberList[idx], plus-1, minus, mul, div)
    if minus > 0:
        dfs(idx+1, s-numberList[idx], plus, minus-1, mul, div)
    if mul > 0:
        dfs(idx+1, s*numberList[idx], plus, minus, mul-1, div)
    if div > 0:
        if s < 0:
            s = (-1) * s
            dfs(idx+1, (s//numberList[idx])*(-1), plus, minus, mul, div-1)
        else:
            dfs(idx+1, s//numberList[idx], plus, minus, mul, div-1)


dfs(1, numberList[0], oper[0], oper[1], oper[2], oper[3])


print(maxAnswer)
print(minAnswer)
