def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    while True:
        if len(A) == 0:
            break
        a = A[-1]
        b = B[-1]

        if a < b:
            answer += 1
            B.pop()

        A.pop()

    return answer
