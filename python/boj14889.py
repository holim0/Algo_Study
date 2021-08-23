from itertools import combinations

n = int(input())

arr = []
answer = 9987654321

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

number = []

for i in range(n):
    number.append(i+1)

johab = list(combinations(number, n//2))


for i in range(len(johab)//2):
    cur_johab = johab[i]
    start, link = 0, 0
    for n in number:
        if n in cur_johab:
            for n2 in number:
                if n2 in cur_johab:
                    start+=arr[n-1][n2-1]
        else:
            for n2 in number:
                if n2 not in cur_johab:
                    link+=arr[n-1][n2-1]

    answer = min(answer, abs(start-link))



print(answer)