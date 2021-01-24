from collections import Counter


def solution(A):

    if len(A) == 1:
        return A[0]

    result = Counter(A)

    for key in result:
        if result[key] % 2 != 0:
            return key
