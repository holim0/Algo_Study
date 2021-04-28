def solution(board, moves):
    answer = 0
    size = len(board)
    
    box = []
    
    stack = []
    
    for j in range(size):
        tmp = []
        for i in range(size):
            
            if board[i][j]!=0:
                tmp.append(board[i][j])
                
        tmp= tmp[::-1]
        
        box.append(tmp)
        

    for i in range(len(moves)):
        cur = moves[i]-1
        
        if len(box[cur])!=0:
            moving_ele = box[cur][-1]
            box[cur].pop()
            
            if len(stack)==0:
                stack.append(moving_ele)
                
            else:
                if stack[-1]==moving_ele:
                    answer+=2
                    stack.pop()
                
                else:
                    stack.append(moving_ele)
        
        
        
        
        
    
    return answer