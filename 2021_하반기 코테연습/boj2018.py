n = int(input())



s, e = 1, 1
sum_val = 1
answer = 0
while s<=e:


    if sum_val==n:
        answer+=1
        sum_val-=s
        s+=1
        
    elif sum_val>n:
        sum_val-=s
        s+=1

    elif sum_val<n:
        e+=1
        sum_val+=e

    


print(answer)