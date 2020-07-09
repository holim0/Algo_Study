

## 그냥 진수 다 구하면 된다 ##

def getzinsu(n, size):
    zinsu="01"
    for i in range(2, size+1):
        
        if(i<n):
            if 9<i<16:
                zinsu+=chr(i+55)
            else:
                zinsu+=str(i)
        else:
            tmp=""
            while True:
                if 16>i%n>9 :
                    tmp+=chr(i%n+55)
                else:
                    tmp+=str(i%n)
                i//=n
                if(i==0): break
                    
            tmp=tmp[::-1]
            zinsu+=tmp
        
        
    return zinsu       




def solution(n, t, m, p):
    answer = ''
    
    tmp= getzinsu(n, t*m)
    
    for i in range(t):
        answer+=tmp[p-1]
        p+=m
    
    
    return answer