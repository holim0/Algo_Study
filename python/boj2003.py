N, M = map(int, input().split())

numArr = []

numArr = list(map(int, input().split()))

answer = 0
start, end = 0, 0


while start < len(numArr) and end < len(numArr):
    if M > sum(numArr[start:end+1]):
        end += 1

    elif M < sum(numArr[start:end+1]):
        start += 1

    elif M == sum(numArr[start:end+1]):
        answer += 1
        end += 1

print(answer)
