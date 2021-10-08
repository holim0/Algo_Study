import sys
input= sys.stdin.readline
t = int(input())


while t:    

    a,b = input().split()
    a_sum, b_sum = 0, 0
    a, b = a[::-1], b[::-1]
    for i in range(len(a)):
        a_sum+= int(a[i]) * 2**i
    
    for i in range(len(b)):
        b_sum+= int(b[i]) * 2**i

    total = a_sum+b_sum


    print(bin(total)[2:])

    

    t-=1