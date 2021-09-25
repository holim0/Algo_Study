n = int(input())

number= list(map(int, input().split()))


sums = [number[0],]


for i in range(1,n):
    
    if sums[i-1]<0:
        sums.append(number[i])
    else:
        sums.append(number[i]+ sums[i-1])

print(max(sums))


