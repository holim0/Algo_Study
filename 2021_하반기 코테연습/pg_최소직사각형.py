import heapq

def solution(sizes):
    answer = 0
    max_h = []
    max_w = []
    
    for s in sizes:
        w, h = s[0], s[1]

        
        if w>h:
            w, h = h, w
        
        heapq.heappush(max_h, -h)
        heapq.heappush(max_w, -w)
    
    answer= heapq.heappop(max_h) *heapq.heappop(max_w)
        
    return answer