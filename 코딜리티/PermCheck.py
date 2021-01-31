def solution(A):

    sort_list = sorted(A)

    for i in range(len(sort_list)):
        if i+1 != sort_list[i]:
            return 0

    return 1
