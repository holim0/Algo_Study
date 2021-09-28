def solution(numbers):
    answer = 0
    
    check  = [False for _ in range(10)]
    
    for n in numbers:
        check[n]=True
        
        
    for i in range(len(check)):
        if not check[i]:
            answer+=i
    
    
    
    return answer