n = int(input())

student = list(map(int, input().split()))

student.sort()
answer = 0

for i in range(len(student)-2):
    cur = student[i]

    l, r = i+1, len(student)-1

    while l<r:

        sum_val = student[l]+student[r] + cur
        if sum_val == 0:
            
            if student[l]==student[r]:
                answer+=(r-l+1) * (r-l)//2
                break
            
            else:
                lc, rc = 1, 1
                while l<r and student[l]==student[l+1]:
                    l+=1
                    lc+=1
        
                while l<r and student[r]==student[r-1]:
                    r-=1
                    rc+=1

                answer+= lc *rc

                r-=1
                l+=1

        elif sum_val > 0:
            r-=1
        elif sum_val < 0:
            l+=1



print(answer)