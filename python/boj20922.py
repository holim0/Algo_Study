import sys
n, k = map(int, input().split())

number = list(map(int, input().split()))

cnt = {}

answer = -sys.maxsize

s, e = 0, 0 

while s<len(number) and e<len(number):

    
    if s==0 and e==0:
        cur = number[s]
        cnt[cur]=1
        answer = max(answer, 1)
        e+=1
        continue


    if number[e] not in cnt:
        cnt[number[e]] = 1
        answer = max(answer, e-s+1)
        e+=1

    else:
        cnt[number[e]]+=1
        if cnt[number[e]]>k:
            while cnt[number[e]]>k:
                cnt[number[s]]-=1
                s+=1
        else:
            answer = max(answer, e-s+1) 
        e+=1

    # print(cnt, s, e)



    

print(answer)


    

