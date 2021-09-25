string = input()

answer= ""

stack =[]
reverse_stack = []


for s in string:


    if len(stack)==0 and s==" ":
        while reverse_stack:
            answer+=reverse_stack.pop()
        answer+=s
        continue

    if s=="<":
        if len(reverse_stack)>0:
            while reverse_stack:
                answer+=reverse_stack.pop()
        stack.append(s)
        answer+=s
        continue

    if len(stack)>0:
        if s==">":
            stack.pop()
            answer+=s

        else:
            answer+=s
    
    elif len(stack)==0:
        reverse_stack.append(s)

if len(reverse_stack)>0:
    while reverse_stack:
        answer+=reverse_stack.pop()

print(answer)
    