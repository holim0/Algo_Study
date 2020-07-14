def solution(n, lost, reserve):
    answer = 0
    
    list=[1 for i in range(n+1)]
    
    for i in range(1,n+1):
        for val in lost:
            if val==i : list[i]-=1
        
        for val2 in reserve:
            if val2==i : list[i]+=1
    
    
    for i in range(1, n+1):
        if list[i]==2:
            if i-1>=1 and list[i-1]==0:
                list[i]=1
                list[i-1]=1
                
            else:
                if i+1<=n and list[i+1]==0:
                    list[i]=1
                    list[i+1]=1
    
    answer= list.count(1)+list.count(2)-1
    return answer