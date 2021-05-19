import sys
n, k = map(int, input().split())


number = list(map(int, input().split()))


answer = -1

def getSol(value):
    global number, answer


    
    if value!="" and int(value)<=n:
        answer = max(answer, int(value))
 
        
    for i in range(len(number)):
        if int(value)+number[i]<=n:
            getSol(value + str(number[i]))

    

    
    



if __name__== "__main__":

    
    
    getSol("0")

    print(answer)

    

    