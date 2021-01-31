global answer
answer = 100


def checkDiffer(a, b):

    cnt = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    return cnt


def getAnswer(cur, target, words, check, count):
    global answer
    if cur == target:
        answer = min(answer, count)
        return

    for idx, w in enumerate(words):
        if checkDiffer(cur, w) == 1:
            if check[idx] == False:
                check[idx] = True
                getAnswer(w, target, words, check, count+1)
                check[idx] = False


def solution(begin, target, words):

    if target not in words:
        return 0

    check = [False for _ in range(len(words))]
    getAnswer(begin, target, words, check, 0)

    global answer

    return answer
