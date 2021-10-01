n =int(input())

answer = 1e100



def isOk(s):

    size = len(s)
    
    for i in range(2, size//2+1):
        if s[size-i:size]==s[size-2*i:size-i]:
            return False

    return True
    

def getSol(cur):
    global answer
    if len(cur)==n:
        print(cur)
        exit(0)

    for i in range(1, 4):
        if cur[-1]==str(i):continue
        next_cur = cur+str(i)
        if isOk(next_cur):
            getSol(next_cur)




getSol("1")


print(answer)