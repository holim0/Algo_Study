import sys
n = int(input())

answer = - sys.maxsize
tmp = input()
number= []
oper = []

for t in tmp:
    if t.isdigit():
        number.append(int(t))

    else:
        oper.append(t)


def getSol(cur_idx, cur_sum):
    global answer

    
    if cur_idx > len(number)-2:
        
        answer= max(answer, cur_sum)
        return 


    if oper[cur_idx]=="+":
        getSol(cur_idx+1, (cur_sum+number[cur_idx+1]))

        if cur_idx+1<len(oper):
            if oper[cur_idx+1]=="-":
                
                getSol(cur_idx+2, cur_sum+(number[cur_idx+1]-number[cur_idx+2]))

            elif oper[cur_idx+1] =="*":
                
                getSol(cur_idx+2, cur_sum+(number[cur_idx+1]*number[cur_idx+2]))

            else:
                getSol(cur_idx+2, (cur_sum+number[cur_idx+1])+number[cur_idx+2])


        

    elif oper[cur_idx]=="-":
        getSol(cur_idx+1, (cur_sum-number[cur_idx+1]))
        if cur_idx+1<len(oper):
            if oper[cur_idx+1]=="+":
                
                getSol(cur_idx+2, cur_sum-(number[cur_idx+1]+number[cur_idx+2]))

            elif oper[cur_idx+1] =="*":
                
                getSol(cur_idx+2, cur_sum-(number[cur_idx+1]*number[cur_idx+2]))
            else:
                getSol(cur_idx+2, cur_sum-(number[cur_idx+1]-number[cur_idx+2]))

    elif oper[cur_idx]=="*":
        getSol(cur_idx+1, (cur_sum*number[cur_idx+1]))
        if cur_idx+1<len(oper):
            if oper[cur_idx+1]=="-":
                
                getSol(cur_idx+2, cur_sum*(number[cur_idx+1]-number[cur_idx+2]))

            elif oper[cur_idx+1] =="+":
                
                getSol(cur_idx+2, cur_sum*(number[cur_idx+1]+number[cur_idx+2]))
            else:
                getSol(cur_idx+2, (cur_sum*number[cur_idx+1])*number[cur_idx+2])



getSol(0, number[0])


print(answer)