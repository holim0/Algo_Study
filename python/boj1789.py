s = int(input())




acc = [1]

answer = 0

i = 1
while True:


    if s-i>=0:
        s-=i
        i+=1
    else:
        break
    
    answer+=1
    
    
print(answer)