from collections import Counter as c
import operator

def solution(genres, plays):
    answer = []
    
    setlist=list(set(genres))
    tmp=[]
    for val in setlist:
        tmp.append([val, 0])
        
    for i in range(len(tmp)):
        for val in range(len(genres)):
            if tmp[i][0]==genres[val]:
                tmp[i][1]+=plays[val]
    
    sortlist = sorted(tmp, key=operator.itemgetter(1), reverse=True)
    
    
    
    for i in range(len(sortlist)):
        arr = []
        for val in range(len(genres)):
            if genres[val] == sortlist[i][0]:
                arr.append([plays[val], val])

        arr.sort(key=lambda x: (-x[0], x[1]))
        
        if len(arr) < 2:
            answer.append(arr[0][1])
        else:

            answer.append(arr[0][1])
            answer.append(arr[1][1])

    return answer