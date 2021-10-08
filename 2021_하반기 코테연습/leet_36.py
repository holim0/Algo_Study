from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        number = []
        
        
        n, m  = len(board), len(board[0])
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j].isdigit():
                    print(board[i][j])
                    number.append((i, j))
        
        def getSol(i, j):
            
            cur = board[i][j]
        
            count = defaultdict(int)
            
            ## 세로
            for x in range(n):
                if board[x][j].isdigit():
                    count[board[x][j]]+=1
            ## 가로    
            for y in range(m):
                if board[i][y].isdigit():
                    count[board[i][y]]+=1
            
            
            start_x, start_y = 3*(i//3), 3*(j//3)

            for x in range(start_x, start_x+3):
                for y in range(start_y, start_y+3):
                    cur_val = board[x][y]
                    
                    if cur_val.isdigit():
                        count[cur_val]+=1
            
            
            if count[cur]>3: return False
            return True
    
        
        
        for val in number:
            x, y = val
            
            if not getSol(x, y):
                return False
            
        
        return True