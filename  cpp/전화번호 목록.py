def solution(phone_book):
    answer = True
    phone_book=sorted(phone_book, key=len)
    
    for i in range(len(phone_book)):
        tmp= phone_book[i]
        for j in range(i+1,len(phone_book)):
            comp= phone_book[j]
            if tmp==comp[0: len(tmp)] :
                return False
            
    
    
    
    return answer