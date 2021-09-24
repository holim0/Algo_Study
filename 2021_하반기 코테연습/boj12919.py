import sys
sys.setrecursionlimit(10000)
S = input()
T = input()

flag = False

def getSol(cur):
    global flag
    
    if cur==S:
        flag =True
        return 

    
    if cur[-1]=="A":
        if len(cur)>=2:
            getSol(cur[:len(cur)-1])

    if cur[0]=="B":
        reverse = "".join(reversed(cur))
        if len(reverse)>=2:
            getSol(reverse[:len(reverse)-1])

    

    



    




if __name__ =="__main__":
    getSol(T)

    if flag:
        print(1)
    else:
        print(0)