from collections import defaultdict
xa, xb = input().split()

MAX = 2**63

a, b = [], []


for x in xa:
    if x.isdigit():
        a.append(int(x))
    else:
        cur = ord(x)-87
        a.append(cur)



for x in xb:
    if x.isdigit():
        b.append(int(x))
    else:
        cur = ord(x)-87
        b.append(cur)

a_max, b_max = max(a), max(b)

possible_a, possible_b = [], []

a, b = a[::-1], b[::-1]

for i in range(a_max+1, 37):
    s = 0
    for j in range(len(a)):
        s+= a[j] * (i**j)

    if s<MAX:
        possible_a.append((i, s))

for i in range(b_max+1, 37):
    s = 0
    for j in range(len(b)):
        s+= b[j] * (i**j)

    if s<MAX:
        possible_b.append((i, s))

answer = []

for pa in possible_a:
    ai, aSum = pa
    for pb in possible_b:
        bi, bSum = pb
        if aSum==bSum and ai!=bi:
            answer.append((aSum, ai, bi))

print(possible_a, "\n", possible_b)

if len(answer)==0:
    print("Impossible")

elif len(answer)>1:
    print("Multiple")

elif len(answer)==1:
    print(answer[0][0], answer[0][1], answer[0][2])








