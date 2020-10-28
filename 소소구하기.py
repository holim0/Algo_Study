import itertools
import math


def sosu(n):

    val = int(math.sqrt(n))+1

    for i in range(2, val):
        if n % i == 0:
            return False

    return True


def solution(nums):
    answer = 0

    per = itertools.combinations(nums, 3)

    perlist = list(per)

    # print(perlist)
    for nlist in perlist:
        sum = 0
        for n in nlist:
            sum += n

        if sosu(sum) == True:

            answer += 1

    return answer
