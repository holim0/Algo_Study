def solution(money):
    answer = 0

    size = len(money)
    dp = [0 for _ in range(size)]
    tmpMax = [0 for _ in range(size)]

    dp2 = [0 for _ in range(size)]
    tmpMax2 = [0 for _ in range(size)]

    dp[1] = money[1]

    dp2[0] = money[0]
    dp2[1] = money[1]

    for i in range(1, size):
        if i == 1:
            tmpMax[i] = money[i]
        elif i == 2:
            dp[i] = money[i]
            tmpMax[i] = max(dp[i], tmpMax[i-1])

        else:
            dp[i] = money[i]+tmpMax[i-2]
            tmpMax[i] = max(tmpMax[i-1], dp[i])

    for i in range(0, size-1):
        if i == 0:
            tmpMax2[i] = money[i]

        elif i == 1:
            dp[i] = money[i]
            tmpMax2[i] = max(dp[i], tmpMax2[i-1])
        else:
            dp[i] = money[i]+tmpMax2[i-2]
            tmpMax2[i] = max(tmpMax2[i-1], dp[i])

    n = max(dp)
    m = max(dp2)

    answer = max(n, m)

    return answer
