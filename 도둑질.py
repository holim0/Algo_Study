def solution(money):
    answer =0
    dp1=[0]*len(money)
    dp2=[0]*len(money)
    
    
    dp1[0]=money[0]
    dp1[1]=money[0]
    
    for i in range(2, len(money)-1):      ##첫번째집 무조건 터는경우
        dp1[i]=max(dp1[i-1], dp1[i-2]+money[i])
        
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2, len(money)):                          ## 마지막집 무조건 터는 경우
        dp2[i]=max(dp2[i-1], dp2[i-2]+money[i])
        
    answer=max(max(dp1), max(dp2))
        
    return answer