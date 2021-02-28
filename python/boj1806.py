n, s = map(int, input().split())

number = list(map(int, input().split()))
size = len(number)
acc = []

acc.append(number[0])


for i in range(1, size):
    acc.append(acc[i-1]+number[i])


start, end = 0, 0

min_len = 100000+5


while True:

    if (end >= size) or start > end:
        break

    curSum = 0
    if start > 0:
        curSum = acc[end]-acc[start-1]
    else:
        curSum = acc[end]

    if curSum < s:
        end += 1

    else:
        length = end-start+1
        min_len = min(min_len, length)
        start += 1


if min_len == (100000+5):
    print(0)
else:
    print(min_len)
