from itertools import combinations
import sys
n = int(input())

answer= sys.maxsize

ele = []

for i in range(n):
    s, b = map(int, input().split())

    ele.append((s, b))


for i in range(1, len(ele)+1):
    johab = list(combinations(ele, i))
    for cur_johab in johab:
        cur_s, cur_b =1, 0
        for j in cur_johab:
            cur_s *=j[0]
            cur_b +=j[1]
    

        diff = abs(cur_s-cur_b)

        answer= min(answer, diff)


print(answer)
