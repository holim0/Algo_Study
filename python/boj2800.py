from itertools import combinations
import copy
s = input()

s = list(s)

bucket = []
pair_bucket = []

answer = []

for i in range(len(s)):
    if s[i] == ")" or s[i] == "(":
        bucket.append((s[i], i))

stack = []

for i in range(len(bucket)):
    if len(stack) == 0:
        stack.append(bucket[i])

    else:
        if stack[-1][0] == "(" and bucket[i][0] == ")":
            pair_bucket.append((stack[-1][1], bucket[i][1]))
            stack.pop()
        else:
            stack.append(bucket[i])

for i in range(1, len(pair_bucket)+1):
    johab_list = combinations(pair_bucket, i)

    for johab in johab_list:
        tmp_s = copy.deepcopy(s)

        for x, y in johab:
            tmp_s[x] = ""
            tmp_s[y] = ""

        result = "".join(tmp_s)
        if result not in answer:
            answer.append(result)


answer.sort()

for s in answer:
    print(s)
