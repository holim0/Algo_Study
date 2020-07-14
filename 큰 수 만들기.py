def solution(number, k):
    answer = ''
    
    
    size=len(number)-k
    start=0
    end=len(number)-size
    
    while True: 
        if end>=len(number):
            break
        maxval=-2  
        base=-1
        for i in range(start, end+1):
            if maxval<int(number[i]):
                maxval=int(number[i])
                base=i
                if maxval==9: break
        
    
        number.replace(number[base], "-1", 1)
        answer+=str(maxval)
        start=base+1
        end+=1
        

        
    
    
    
    
    return answer