import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    
    heap=[]
    
    list=[]
    
    for a, b in zip(dates, supplies):
        list.append([a, b])
    
    
    list.sort(reverse=True)
    
    
    while stock < k:
        while len(list) > 0 and list[len(list)-1][0] <= stock: 
            heapq.heappush(heap, -list[len(list)-1][1])
            list.pop()
        
        stock += -heapq.heappop(heap)
        answer += 1


    
    
    return answer