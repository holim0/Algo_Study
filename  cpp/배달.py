Max = 987654321
dp = [[Max] * 55 for i in range(55)]


def solution(N, road, K):
    answer = 0

    for i in range(1, N+1):
        dp[i][i] = 0

    for f, t, cost in road:
        if dp[f][t] >= cost:
            dp[f][t] = cost
            dp[t][f] = cost

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    for i in range(1, N+1):
        if dp[1][i] <= K or dp[i][1] <= K:

            answer += 1

    return answer
