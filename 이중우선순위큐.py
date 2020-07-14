import heapq as h

def solution(operations):
    answer = []
    
    heap=[]
    
    for val in operations:
        tmp=val.split(' ')
        if tmp[0]=='I':
            h.heappush(heap,int(tmp[1]))
        elif len(heap)>0 and tmp[0]=='D' and tmp[1]=='1':
            heap.remove(max(heap))
            h.heapify(heap)
        
        elif len(heap)>0 and tmp[0]=='D' and tmp[1]=='-1' :
            h.heappop(heap)
        
        
    
     
        
    if len(heap)==0:
        return [0, 0]
        
        
    answer.append(max(heap))
    answer.append(h.heappop(heap))    
    return answer


