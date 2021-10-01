n = int(input())

number = list(map(int, input().split()))

check = [False for _ in range(n)]


answer = 0

johab = []

def getSol(curidx, cur_johab):
    global answer

    if len(cur_johab)==3 and cur_johab[1]-cur_johab[0]==cur_johab[2]-cur_johab[1]:
        answer+=1
        return


    for i in range(curidx+1, len(number)):
        if len(cur_johab)<2 and not check[i]:
            check[i] = True
            cur_johab.append(number[i])
            getSol(i, cur_johab)
            check[i] = False
            cur_johab.pop()

        elif not check[i]:
            if cur_johab[1]-cur_johab[0] == number[i]-cur_johab[1]:
                check[i] = True
                cur_johab.append(number[i])
                getSol(i, cur_johab)
                check[i] = False
                cur_johab.pop()
            





for i in range(0, n-3):
    check[i] = True
    getSol(i, [number[i]])
    check[i] = False


print(answer)