def solution(A):

    set_list = set(A)

    sort_list = sorted(list(set_list))

    answer = 1

    for val in sort_list:

        if val == answer:
            answer += 1

    return answer
