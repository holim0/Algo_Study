import sys
from collections import deque
n = int(input())

milk = []

dx = [1, 0]
dy = [0, 1]

mapping = {
    0: 1,
    1: 2,
    2: 0
}



dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]


for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    milk.append(tmp)


def check_range(x, y):
    global n

    if x>=0 and x<n and y>=0 and y<n:
        return True
    
    return False



for i in range(n):
    for j in range(n):
        
        if milk[i][j]==0:
            dp[i][j][0] = max(dp[i][j][0], 1)        
            
                
        
        for k in range(2):
            nx, ny = i+dx[k], j+dy[k]
            
            if check_range(nx, ny):
                cur_milk= milk[nx][ny] ## 다음 우유
                for w in range(3):
                    if mapping[w] == cur_milk and dp[i][j][w]!=0:
                        dp[nx][ny][cur_milk]  = max(dp[nx][ny][cur_milk], dp[i][j][w]+1)
                    else:
                        dp[nx][ny][w] = max(dp[nx][ny][w], dp[i][j][w])



print(max(dp[n-1][n-1]))





