def solution(A):

    sum_1 = sum(A)

    sum_2 = 0

    for i in range(1, len(A)+2):

        sum_2 += i

    return sum_2-sum_1
