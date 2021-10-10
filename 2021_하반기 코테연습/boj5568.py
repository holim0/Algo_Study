from itertools import permutations as permu
n = int(input())
k = int(input())

answer = set()


number= []

for _ in range(n):
    tmp = input()
    number.append(tmp)


per = list(permu(number, k))

for p in per:

    list_p = list(p)

    cur_n = "".join(list_p)

    answer.add(int(cur_n))


print(len(answer))
