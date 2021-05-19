s  =input()


stack= []

answer =0

tmp = 0

dp = [[0 for _ in range(len(s))] for _ in range(len(s))]


def getSol(start, end):
    
    if start>end:
        return 1

    stack = []
    value = 0
    now = start
    for i in range(start, end+1):
        if len(stack)==0:
            stack.append(s[i])

        else:

            if s[i]==")" and stack[-1]=="(":
                stack.pop()
                if len(stack)==0:
                    value += 2*getSol(now+1, i-1)
                    now = i+1

            elif s[i]=="]" and stack[-1]=="[":
                stack.pop()
                if len(stack)==0:
                    
                    value += 3*getSol(now+1, i-1)
                    now = i+1
                    
                    
            
            else: stack.append(s[i])

    
    return value

    
def check_s(s):

    sck=[]


    for i in range(len(s)):

        if len(sck)==0:
            sck.append(s[i])

        else:
            if s[i]==")" and sck[-1]=="(":
                sck.pop()

            elif s[i]=="]" and sck[-1]=="[":
                sck.pop()

            else:
                sck.append(s[i])


    if len(sck)==0:
        return True
    
    else:
        return False
 
           
        


if __name__ == '__main__':

    if not check_s(s):
        print(0)
    else:

        answer = getSol(0, len(s)-1) 
        print(answer) 
    






