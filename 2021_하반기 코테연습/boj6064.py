import sys

input = sys.stdin.readline


T = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


while T:

    M, N, x, y = map(int, input().split())

    l = lcm(M, N)
    flag = False
    for i in range(x, l+1, M):
        tmp = -1
        if i%N==0:
            tmp = N
        else:
            tmp =i%N
        
        if tmp==y:
            print(i)
            flag= True
            break
        
       
    if not flag:
        print(-1)
    T-=1