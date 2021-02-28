import sys
from itertools import combinations
n, k = map(int, input().split())

frontAndEnd = "antatica"

words = []

alpa = []

for s in list(frontAndEnd):
    if s not in alpa:
        alpa.append(s)

for i in range(n):
    s = sys.stdin.readline()
    s.rstrip('\n')
    new_s = s[4: len(s)-5]
    words.append(new_s)

if k < 5:
    print(0)
    exit(0)


for word in words:
    for s in list(word):
        if s not in alpa:
            alpa.append(s)


answer = 0


k = k-5

if len(alpa[5:]) <= k:
    tmp = 0
    for word in words:
        flag = False
        for s in list(word):
            if s not in alpa:
                flag = True
                break

        if not flag:
            tmp += 1

    answer = max(tmp, answer)

else:
    for johab in combinations(alpa[5:], k):
        tmp = 0

        for word in words:
            flag = False
            for s in list(word):
                if (s not in alpa[:5]) and (s not in johab):
                    flag = True
                    break

            if not flag:
                tmp += 1

        answer = max(tmp, answer)

print(answer)
