import sys
n, m = map(int, input().split())

arr = []


for i in range(n):

    string, number = sys.stdin.readline().split()
    arr.append((string, int(number)))



for i in range(m):
    attack = int(sys.stdin.readline())
    
    answer=""

    l, r= 0, len(arr)-1

    while l <= r:

        mid = (l+r)//2

        mid_text, mid_number = arr[mid]


        if attack<=mid_number:
            answer= mid_text
            r= mid-1

        else:
            l = mid+1

    print(answer)

