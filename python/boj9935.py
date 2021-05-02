from collections import deque

string = input()

explosion = input()
exlen = len(explosion)

string.rstrip("\n")
explosion.rstrip("\n")

stack= []
cur = deque([])


    

for s in string:
   
    stack.append(s)
    
    if len(cur)<exlen:
        cur.append(s)
    else:
        cur.popleft()
        cur.append(s)
    
    if len(cur)==exlen:
        if "".join(cur)==explosion:
            for i in range(exlen):
                stack.pop()

            cur = deque([])
            if len(stack)==0: continue

            elif len(stack)>=exlen:
                for i in range(exlen):
                    cur.append(stack[len(stack)-exlen+i])

            else:
                for i in range(len(stack)):
                    cur.append(stack[i])





if len(stack)==0:
    print("FRULA")

else:
    print("".join(stack))