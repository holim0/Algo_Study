import sys

t= int(sys.stdin.readline())

first = [1, 3, 6, 10, 15, 21]
first_money= [5000000, 3000000, 2000000, 500000, 300000, 100000]
second = [1, 3, 7, 15, 31]
second_money= [5120000, 2560000, 1280000, 640000, 320000]

while t:

    a, b = map(int, sys.stdin.readline().split())


    a_sum =0

    b_sum =0

    if a<=21 and a!=0:
        for i in range(len(first)):
            if a<=first[i]:
                a_sum= first_money[i]
                break


    if b<=31 and b!=0:
        for i in range(len(second)):
            if b<=second[i]:
                b_sum= second_money[i]
                break

    
    print(a_sum+b_sum)

    t-=1