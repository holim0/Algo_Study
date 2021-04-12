import sys

t = int(input())

dict ={
    2 : [1],
    3 : [7],
    4 : [4],
    5: [2, 3, 5 ],
    6: [0,6,9],
    7: [8]
}

how_many ={
    0: 6,
    1:2,
    2:5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}


dp = [[sys.maxsize ,-1] for _ in range(102)]


dp[2][0], dp[2][1] = 1, 1

for i in range(3, 101):
    min_tmp, max_tmp = 0, 0
    for j in range(1, i):
        if dp[i-j][0] > 0 and dp[j][0] > 0:

            min_tmp = str(dp[i-j][0]) + str(dp[j][0])
            min_tmp = int(min_tmp)

            dp[i][0] = min(dp[i][0], min_tmp)

        if dp[i-j][1]>0 and dp[j][1]>0:
            max_tmp = str(dp[i-j][1]) +str(dp[j][1])
            max_tmp = int(max_tmp)
            dp[i][1] = max(dp[i][1], max_tmp)

    
    
    if i in dict:
        dp[i][0] = min(min(dict[i]), dp[i][0])
        if dp[i][0] ==0:
            dp[i][0] = dict[i][1]
        dp[i][1] = max(max(dict[i]), dp[i][1])
    
    str_min = list(str(dp[i][0]))
    for j in range(1,len(str_min)):
        key = int(str_min[j])
        number_key = how_many[key]
        
        str_min[j] = str(dict[number_key][0])

    dp[i][0] = int("".join(str_min))

while t>0:

    n =int(input())


    print(dp[n][0], dp[n][1])




    t-=1