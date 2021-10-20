import sys
from itertools import combinations
n, k = map(int, input().split())

frontAndEnd = "antatica"

words = []

alpa = []

for i in range(n):
    s = sys.stdin.readline()
    new_s = s[4: len(s)-5]
    words.append(new_s)

if k < 5:
    print(0)
    exit(0)

anta =["a", "n", "t", "i", "c"]
for word in words:
    for s in list(word):
        if s not in alpa and s not in anta:
            alpa.append(s)


answer = 0


k = k-5

if len(alpa)<k:
    tmp =0
    for word in words:
        flag = False
        for s in list(word):
            if len(alpa)>0:
                if s not in anta and s not in alpa:
                    flag = True
                    break
            else:
                if s not in anta:
                    flag = True
                    break

        if not flag:
            tmp += 1

    answer = max(tmp, answer)


for johab in combinations(alpa, k):
    tmp = 0
    
    for word in words:
        flag = False
        for s in list(word):
            
            if (s not in anta) and (s not in johab):
                flag = True
                break

        if not flag:
            tmp += 1

    answer = max(tmp, answer)

print(answer)


