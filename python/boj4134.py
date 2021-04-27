import sys
from math import sqrt
t = int(input())

def isSosu(number):

    if number ==0 or number==1:
        return False

    
    for i in range(2, int(sqrt(number)+1)):
        if number%i==0:
            return False

    return True

while t>0:

    n = int(sys.stdin.readline())

    answer= n
    
    while True:
        if isSosu(answer):
            print(answer)
            break

        answer+=1

    

    t-=1