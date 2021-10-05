from collections import defaultdict

n, k = map(int, input().split())

answer = []

after_k = list(map(int, input().split()))

d = list(map(int, input().split()))




for _ in range(k):
    tmp = [0] *n
    for i in range(n):
        tmp[d[i]-1] = after_k[i] 

    after_k = tmp



for i in range(n):
    print(after_k[i],end=" ")


