import sys

n = int(input())

answer = 0

str_list = []

for i in range(n):
    s = sys.stdin.readline()
    str_list.append(s.rstrip("\n"))


dict = {}

for strMember in str_list:
    factor = len(strMember)-1
    for s in strMember:

        if s in dict:
            dict[s] += pow(10, factor)
        else:
            dict[s] = pow(10, factor)

        factor -= 1


arr = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for i in range(len(arr)):
    answer += arr[i][1] * (9-i)


print(answer)
