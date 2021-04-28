def solution(N):
    answer = 0
    fibo=[1, 1]
    for i in range(2, N):
        fibo.append(fibo[i-1]+fibo[i-2])
        
    
    answer=2*(fibo[N-1]+fibo[N-1]+fibo[N-2])
    return answer