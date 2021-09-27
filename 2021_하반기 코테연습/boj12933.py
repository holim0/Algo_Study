sound = input()

arr = []
answer = 0

isOver = False

for s in sound:


    if s=="q":
        flag = False
        for i in range(len(arr)):
            if arr[i][-1] =="k":
                arr[i]+=s
                flag = True
                break

        if not flag:
            arr.append(s)

    elif s=="u":
        flag = False
        for i in range(len(arr)):
            if arr[i][-1]=="q":
                arr[i]+=s
                flag = True
                break

        if not flag:
            print(-1)
            isOver = True
            break


    elif s=="a":
        flag = False
        for i in range(len(arr)):
            if arr[i][-1]=="u":
                arr[i]+=s
                flag = True
                break

        if not flag:
            print(-1)
            isOver = True
            break

    elif s=="c":
        flag = False
        for i in range(len(arr)):
            if arr[i][-1]=="a":
                arr[i]+=s
                flag = True
                break

        if not flag:
            print(-1)
            isOver = True
            break

    elif s=="k":
        flag = False
        for i in range(len(arr)):
            if arr[i][-1]=="c":
                arr[i]+=s
                flag = True
                break

        if not flag:
            print(-1)
            isOver = True
            break


if not isOver:
    cnt = 0
    f = False
    for a in arr:
        if len(a)%5!=0:
            print(-1)
            f = True
            break
        else:
            cnt+=1

    if not f:
        print(cnt)
