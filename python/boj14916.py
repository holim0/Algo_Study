n = int(input())


answer =0


while n>0:

    
    if n>=5:
        next_val = n-5
        if next_val>=5:
            answer+=1
            n = next_val

        else:
            if next_val%2==0:
                answer+=next_val//2+1
                break
                
            else:
                n = n-2
                answer+=1
                    

    else:
        if n%2==0:
            answer+=n//2
        else:
            answer= -1
        break

print(answer)