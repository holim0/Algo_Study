class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        dx =[1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        self.isAnswer = False
    
        
        n, m = len(board), len(board[0])
        
        visit = [[False for _ in range(m)] for _ in range(n)]
        
        def check_range(x, y):
            if x>=0 and x<n and y>=0 and y<m:
                return True
            return False
        
        
        def getSol(x,y, cur, idx, cur_visit):
            if idx==len(word):
                self.isAnswer = True
                return
                
            
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                
                if check_range(nx, ny) and not cur_visit[nx][ny]:
                    if board[nx][ny]==word[idx]:
                        cur_visit[nx][ny]=True
                        getSol(nx, ny, cur+board[nx][ny], idx+1, cur_visit)
                        cur_visit[nx][ny]=False
                        
            
            
        
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    visit[i][j]=True
                    getSol(i, j, board[i][j], 1, visit)
                    visit[i][j]=False
                
        
        
        if self.isAnswer: return True
        return False
            
            
            