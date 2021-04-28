def solution(s):
    answer = []
    arr=[]
    tmp=s.split('},{')
    idx=0
    for val in tmp:
        n=val.split(',')
        arr.append([])
        for i in n:
            i=i.replace("}", "")
            i=i.replace("{", "")
            arr[idx].append(i)
        idx+=1   
    
    
    for val in arr:
        val.insert(0, len(val))
    arr.sort()
    
    for val in arr:
        for i in range(1, len(val)):
            if int(val[i]) not in answer:
                answer.append(int(val[i]))
                
    return answer







    ##########정규 표현식을 쓴 다른 사람의 풀이 ################

#     import re
# from collections import Counter


# def solution(s):

#     s = Counter(re.findall('\d+', s))
#     print(s)
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

