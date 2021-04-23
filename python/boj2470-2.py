import sys
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

s, e = 0, len(arr)-1

min_val = sys.maxsize

ans_x, ans_y = 0, 0

while s<e:

    cur = abs(arr[s]+arr[e])

    if cur<min_val:
        min_val = cur
        ans_x = arr[s]
        ans_y = arr[e]

    
    if abs(arr[s]) >abs(arr[e]):
        s+=1
    else:
        e-=1
    

answer = [ans_x, ans_y]
answer.sort()

for a in answer:
    print(a, end=" ")

