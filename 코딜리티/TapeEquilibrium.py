def solution(A):

    arr = A

    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    answer = abs(arr[0]-(arr[-1]-arr[0]))

    for i in range(1, len(arr)-1):
        p1 = arr[i]
        p2 = arr[-1]-arr[i]

        answer = min(answer, abs(p1-p2))

    return answer
