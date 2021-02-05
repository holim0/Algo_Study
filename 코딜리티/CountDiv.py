def solution(A, B, K):

    if A % K == 0:
        answer = (B//K)-(A//K)+1

    else:
        answer = (B//K)-(A//K)

    return answer
