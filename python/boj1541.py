import re
from collections import deque

string = input()

answer =0

number = re.split('[+ | -]', string)
oper = []

s1 = deque([])
s2 = deque([])

for s in string:
    if not s.isdigit():
        oper.append(s)

if len(oper)==0:
    print(number[0])
    exit(0)



for i in range(len(number)):
    if i ==0:
        s1.append(int(number[i]))
        s2.append(oper[i])
    

    else:
        if s2[-1]=="-":
            s1.append(int(number[i]))
            if i!=len(number)-1:
                s2.append(oper[i])
            

        else:
            tmp = s1.pop()
            s1.append(tmp+int(number[i]))
            s2.pop()
            if i!=len(number)-1:
                s2.append(oper[i])


answer = s1.popleft()
while s1:
    
    answer-=s1.popleft()


print(answer)