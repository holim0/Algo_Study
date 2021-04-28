def solution(brown, yellow):
    answer = []
    total= brown+yellow
    
    for i in range(1, total+1):
        if total%i==0 and total//i <=i:
            if 2*(i+int(total//i))-4==brown:
                answer.append(i)
                answer.append(int(total//i))
                break
    
    return answer