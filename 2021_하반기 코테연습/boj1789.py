s = int(input())


def getSum(x, y):

    return ((y-x+1) * (x+y)) //2


start, end = 1, s
answer = -1

while start<=end:

    mid = (start+end)//2
    
    
    if getSum(1, mid)>s:
        end = mid-1

    else:
        answer= mid
        start = mid+1


print(answer)
