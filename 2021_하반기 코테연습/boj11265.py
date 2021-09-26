import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

link =[]

for i in range(n):
    cost = list(map(int, input().split()))
    link.append(cost)
        

customer = []



ENJOY ="Enjoy other party"
STAY = "Stay here"


for k in range(n):
    for i in range(n):
        for j in range(n):
            link[i][j] = min(link[i][j], link[i][k]+link[k][j])



def getSol(start, end, time):
    
    return link[start-1][end-1]<=time
   



for _ in range(m):
    a, b, c = map(int, input().split())

    if getSol(a, b, c):
        print(ENJOY)
    else:
        print(STAY)
    