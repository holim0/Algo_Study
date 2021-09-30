from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

while t:

    oper = input().rstrip("\n")
    
    arr = deque([])
    n = int(input())
    str_arr = input()
    isErr = False

    str_arr = str_arr[1:len(str_arr)-2].split(",")
    
    
    if n==0:
        str_arr = []
        
    pointer = True
    
    for s in str_arr:
        arr.append(s)
    
    for o in oper:
        
        if o=="R":
            pointer = not pointer
            
        elif o=="D":
            if len(arr)==0:
                isErr = True
                break
            else:
                if pointer==True:
                    arr.popleft()
                else:
                    arr.pop()


    if isErr:
        print("error")

    else:
        if pointer ==True:
            answer= ",".join(arr)
            answer = "["+answer+"]"
        else:
            arr.reverse()
            answer= ",".join(arr)
            
            
            
            answer = "["+answer+"]"
        
       
        print(answer)

    t-=1