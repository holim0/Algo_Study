t = int(input())

while t:

    n = int(input())


    dp = [0 for _ in range(n+1)]


    dp[0], dp[1] = 1, 1


    for i in range(1, 4):

        for j in range(2, n+1):
            if j-i>=0:
                dp[j] += dp[j-i]
        



    print(dp[n])


    t-=1