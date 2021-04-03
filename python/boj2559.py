import sys
n, k  =map(int, input().split())


answer = -sys.maxsize
arr = list(map(int, input().split()))


sum_arr = [arr[0],]

for i in range(1, len(arr)):
    sum_arr.append(sum_arr[-1]+ arr[i])


for i in range(len(arr)-k+1):
    if i==0:
        sumVal= sum_arr[i+k-1]
        answer =max(answer, sumVal)

    else:
        sumVal = sum_arr[i+k-1] -sum_arr[i-1]
        answer = max(answer, sumVal)


print(answer)
