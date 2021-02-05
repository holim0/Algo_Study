def solution(N, number):

    if N == number:
        return 1
    arr = [[] for _ in range(10)]

    arr[1].append(N)

    for i in range(2, 9):
        if int(str(N)*i) == number:
            return i
        arr[i].append(int(str(N)*i))
        for idx in range(1, i//2+1):
            for a in arr[idx]:
                for b in arr[i-idx]:
                    if a+b == number or a-b == number or a*b == number or b-a == number:
                        return i
                    if b != 0 and a//b == number:
                        return i
                    if a != 0 and b//a == number:
                        return i
                    arr[i].append(a+b)
                    arr[i].append(a-b)
                    arr[i].append(b-a)
                    arr[i].append(a*b)
                    if b != 0:
                        arr[i].append(a//b)
                    if a != 0:
                        arr[i].append(b//a)

    return -1
