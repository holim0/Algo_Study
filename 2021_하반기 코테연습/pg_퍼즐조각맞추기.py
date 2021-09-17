from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y, size):
    
    if x>=0 and x<size and y>=0 and y<size:
        return True
    return False


def get_puzz(table):
    global dx, dy
    size = len(table)
    q = deque()
    puzz=[]
    visit = [[False for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if table[i][j] ==1 and visit[i][j]== False:
                visit[i][j] = True
                tmp = []
                tmp.append((i, j))
                q= deque([(i, j)])
                while q:
                    cx, cy = q.popleft()
                    for k in range(4):
                        nx, ny = cx+dx[k], cy+dy[k]

                        if check_range(nx, ny, size) and table[nx][ny]==1 and visit[nx][ny]==False:
                            visit[nx][ny] = True
                            tmp.append((nx, ny))
                            q.append((nx, ny))
                puzz.append(tmp)
    
    return puzz
                
    
def get_empty(table):
    global dx, dy
    size = len(table)
    q = deque()
    emp=[]
    visit = [[False for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if table[i][j] ==0 and visit[i][j]== False:
                visit[i][j] = True
                tmp = []
                tmp.append((i, j))
                q= deque([(i, j)])
                while q:
                    cx, cy = q.popleft()
                    for k in range(4):
                        nx, ny = cx+dx[k], cy+dy[k]

                        if check_range(nx, ny, size) and table[nx][ny]==0 and visit[nx][ny]==False:
                            visit[nx][ny] = True
                            tmp.append((nx, ny))
                            q.append((nx, ny))
                emp.append(tmp)
    
    return emp
    
def move(mapp):
    
    fx, fy = mapp[0]
    new_mapp = []
    for m in mapp:
        m = m[0]-fx, m[1]-fy
        new_mapp.append((m))
        
    
    return sorted(new_mapp)
    
def rotate(puzz, n):
    
    new_puzz = []
    
    for p in puzz:
        new_puzz.append((p[1], n-p[0]-1))
    
    new_puzz.sort()
    moved_puzz = move(new_puzz)
    
    return sorted(moved_puzz)
    
    
def check_same(emp, puzz, size):
    
    ## 원본 비교
    emp.sort()
    puzz.sort()
    
    emp = move(emp)
    puzz = move(puzz)
    
    if emp==puzz:
        return True
    
    
    for i in range(3):
        rota_puzz = rotate(puzz, size)
        if rota_puzz == emp:
            return True
        else:
            puzz = rota_puzz
    
    return False
        
    
def solution(game_board, table):
    answer = 0
    
    puzz = []
    empty = []
    
    
    puzz = get_puzz(table)
    empty = get_empty(game_board)
    puzz_check = [False for _ in range(len(puzz))]
    emp_check = [False for _ in range(len(empty))]
    
    for i in range(len(empty)):
        cur_empty = empty[i]
        if emp_check[i]: continue
            
        for j in range(len(puzz)):
            cur_puzz = puzz[j]
            if puzz_check[j] or emp_check[i]: 
                continue
            else:
                if check_same(cur_empty, cur_puzz, len(table)):
                    print(cur_empty, cur_puzz)
                    emp_check[i] = True
                    puzz_check[j] = True

                    answer+=len(cur_puzz)
                
        
    print(answer)
    return answer