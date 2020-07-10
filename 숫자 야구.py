def solution(baseball):
    answer = 0
    su=[]
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i!=j and i!=k and j!=k :
                    su.append(100*i+10*j+k)
                
    
    for i in su:
        tmp=str(i)
        isbreak=False
        for a, b, c in baseball:
            val=str(a)
            # print(tmp, val)
            st=0
            ball=0
            for n1 in range(len(tmp)):
                for n2 in range(len(val)):
                    if n1==n2 and tmp[n1]==val[n2]:
                        st+=1
                    elif n1!=n2 and tmp[n1]==val[n2]:
                        ball+=1
            # print("st: ", st, "ball:", ball)            
            if st==b and ball==c: 
                continue
            else:
                isbreak=True
                break
        
        if isbreak==False:
            answer+=1
    
    
    
    
    
    
    return answer