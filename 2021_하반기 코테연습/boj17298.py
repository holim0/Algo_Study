from collections import deque
n = int(input())

number= list(map(int, input().split()))

stack = deque([(number[0], 0)])


idx =1

answer= [-1 for _ in range(n)]
while idx<n:
    
        
    while True:
        
        if len(stack)>0 and stack[-1][0]<number[idx]:
            curidx = stack[-1][1]
            answer[curidx]=number[idx]
            stack.pop()
        else:
            break

    stack.append((number[idx], idx))
    idx+=1      
            
        



for a in answer:
    print(a, end=" ")

