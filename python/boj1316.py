n = int(input())

answer = 0
while n>0:

    string = input()
    isValid = True
    new_s = []

    for s in string:
        if len(new_s)==0:
            new_s.append(s)
        
        else:
            if new_s[-1]!= s:
                new_s.append(s)
    
    dict = {}

    for i in range(len(new_s)):
        if new_s[i] not in dict:
            dict[new_s[i]] =1
        else:
            isValid = False
            break

    if isValid:
        answer+=1
        
    n-=1

print(answer)