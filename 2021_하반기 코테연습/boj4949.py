
while True:

    val = input()

    if val ==".": break
    stack =[]

    for s in val:
        
        if s =="(" or s=="[":
            stack.append(s)

        elif s==")":
            if len(stack)>0 and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(s)

        elif s=="]":
            if len(stack) >0 and stack[-1]=="[":
                stack.pop()
            else:
                stack.append(s)

    
    if len(stack)==0:
        print("yes")
    else:
        print("no")