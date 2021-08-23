N = int(input())

answer  = 0

A = list(map(int, input().split()))


B, C = map(int, input().split())


for i in range(len(A)):
    cur = A[i]
    cur -= B
    answer+=1
    
    if cur>0:
        mock = cur // C
        
        if cur % C != 0:
            answer+=(mock+1)
        else:
            answer+=mock
    


print(answer)