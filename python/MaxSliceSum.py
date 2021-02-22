def solution(A):

    partsum = 0
    maxSum = -1000000

    for n in A:
        maxSum = max(maxSum, partsum+n)
        partsum = max(0, partsum+n)

    return maxSum
