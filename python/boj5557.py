import sys

n = int(input())


answer = 0

number= list(map(int, sys.stdin.readline().split()))


target = number[-1]



memo = [[0 for _ in range(200)] for _ in range(200)]

def getSol(cur, idx):
    global target, answer, memo
    
    if idx==len(number)-1:
        if cur==target:
            return 1
        else: return 0 

    if memo[cur][idx]!= 0:
        return memo[cur][idx]
    
    
    if cur+number[idx]<=20: memo[cur][idx]+=getSol(cur+number[idx], idx+1)

    if cur-number[idx]>=0: memo[cur][idx]+=getSol(cur-number[idx], idx+1)

    return memo[cur][idx]


if __name__ == '__main__':
    
    print(getSol(number[0], 1))



