n = int(input())

d = list(map(int, input().split()))

gas = list(map(int, input().split()))

answer = 0

min_val = gas[0]

for i in range(len(gas)-1):
    if gas[i]<min_val:
        min_val = gas[i]
    
    answer+=min_val* d[i]


print(answer)