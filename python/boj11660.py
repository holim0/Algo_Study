import sys
n, m = map(int, input().split())

number = []

for i in range(n):

    tmp= list(map(int, sys.stdin.readline().split()))

    number.append(tmp)


acc_number = []

for i in range(n):
    
    acc_tmp = [number[i][0]]

    
    for j in range(1,n):
        acc_tmp.append(acc_tmp[-1]+number[i][j])


    acc_number.append(acc_tmp)





for i in range(m):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    
    answer = 0

    for i in range(x1, x2+1):
        
        if y1==0:
            answer+=acc_number[i][y2]

        else:
            answer+=acc_number[i][y2] - acc_number[i][y1-1]



    
    print(answer)
