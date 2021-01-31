def solution(N, A):

    counter = [0 for _ in range(N)]

    counter_max = 0
    base_max = 0
    for a in A:
        if a <= N:

            if counter[a-1] <= base_max:
                counter[a-1] = base_max+1
            else:
                counter[a-1] += 1

            counter_max = max(counter_max, counter[a-1])
        if a == N+1:
            base_max = counter_max

    for key in range(len(counter)):
        if counter[key] < base_max:
            counter[key] = base_max

    return counter
