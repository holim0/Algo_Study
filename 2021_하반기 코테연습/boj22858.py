from collections import defaultdict
import copy
n, k = map(int, input().split())

answer = []

after_k = list(map(int, input().split()))

d = list(map(int, input().split()))

change_dic = defaultdict(int)


for i in range(len(d)):
    change_dic[i] = d[i]-1 ## i를 d[i]-1로



for _ in range(k):
    tmp = [0 for _ in range(n)]
    for i in range(n):
        tmp[change_dic[i]] = after_k[i] 

    after_k = copy.deepcopy(tmp)



for i in range(n):
    print(after_k[i],end=" ")


