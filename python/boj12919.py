s = input()
t = input()

isOk = False

def getSol(cur):
    
    global isOk
    
    if len(cur)==len(s):
        
        if cur == s:
            print(1)
            exit(0)
        
        return

    
    if cur[0]=="A" and cur[-1]=="B":
        return 

    if cur[-1]== "A":
        next = cur[:len(cur)-1]
        getSol(next)

    if cur[0]=="B":
        next  = cur[::-1]
        next = next[:len(next)-1]
        getSol(next)
    

    

            






if __name__ == "__main__":
    getSol(t)
    
    
    print(0)