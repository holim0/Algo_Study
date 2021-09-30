n = int(input())

col = [-1 for _ in range(n)]
answer= 0

def isOk(cur_number):
    global col
    for i in range(cur_number):
        if (col[cur_number]==col[i]) or (abs(col[cur_number]-col[i]) == abs(cur_number-i)):
            return False

    return True


def getSol(cur_row_number):
    global answer, col

    
    if cur_row_number==n:
        answer+=1
        return 
    
    
    for i in range(n):
        col[cur_row_number] = i
        if isOk(cur_row_number):
            getSol(cur_row_number+1)


    



getSol(0)


print(answer)