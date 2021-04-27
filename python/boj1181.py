import sys
n = int(input())


arr= []


for i in range(n):

    s = input()
    if s not in arr:
        arr.append(s)


sorted_arr = sorted(arr, key=lambda x : (len(x), x))

for s in sorted_arr:
    print(s)