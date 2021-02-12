from itertools import permutations

k = int(input())

oper = list(input().split())

size = len(oper)

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

need_n = size+1

permu_list = list(permutations(num, need_n))

minAnswer = 98765432198
maxAnswer = -1

for n in permu_list:
    flag = True

    for i in range(len(n)-1):
        if oper[i] == ">":
            if n[i] > n[i+1]:
                continue
            else:
                flag = False
                break
        else:
            if n[i] < n[i+1]:
                continue
            else:
                flag = False
                break

    if flag:
        tmp = int("".join(map(str, n)))
        minAnswer = min(minAnswer, tmp)
        maxAnswer = max(maxAnswer, tmp)

if len(str(maxAnswer)) < need_n:
    print("0"+str(maxAnswer))
else:
    print(str(maxAnswer))

if len(str(minAnswer)) < need_n:
    print("0"+str(minAnswer))
else:
    print(str(minAnswer))
