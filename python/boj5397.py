import sys
t = int(input())


while t>0:

    s = sys.stdin.readline()
    s= s.rstrip("\n")
    answer =""

    
    stack1 = []
    stack2 = []
    for i in range(len(s)):
        cur = s[i]

        if cur=="<":
            if len(stack1)>0:
                stack2.append(stack1[-1])
                stack1.pop()

        elif cur ==">":
            if len(stack2)>0:
                stack1.append(stack2[-1])
                stack2.pop()
        elif cur =="-":
            if len(stack1)>0:
                stack1.pop()

        else:
            stack1.append(cur)
       
    
    answer = "".join(stack1)

    stack2 = stack2[::-1]

    answer+= "".join(stack2)


    print(answer)

    t-=1