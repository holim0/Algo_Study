import heapq as h


def solution(scoville, K):
    answer = 0

    h.heapify(scoville)
        
    while scoville[0] < K:
        if len(scoville)==1 and scoville[0]<K:
            return -1
        answer+=1
        n1= h.heappop(scoville)
        n2= h.heappop(scoville)
        
       
        h.heappush(scoville, n1+2*n2)
        
        
    return answer