t = int(input())

while t:

    N = int(input())

    coin = list(map(int, input().split()))

    M = int(input())


    dp = [0 for _ in range(M+1)]

    dp[0] = 1

    for i in range(len(coin)):
        for j in range(1, M+1):
            if j-coin[i]>=0:
                dp[j]+=dp[j-coin[i]]
    
    print(dp[M])




    t-=1