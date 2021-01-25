def solution(X, A):

    check = [False for _ in range(X+1)]

    s = 0
    for i in range(1, X+1):
        s += i

    for i in range(len(A)):
        pos = A[i]
        if check[pos] == False:
            check[pos] = True
            s -= pos
            if s == 0:
                return i

    if s != 0:
        return -1
