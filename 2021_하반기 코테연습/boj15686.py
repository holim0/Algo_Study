from itertools import combinations

n, m = map(int, input().split())

mapp = []

answer = 987654321

for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

chick = []
home = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            home.append((i, j))
        elif mapp[i][j] ==2:
            chick.append((i, j))

johab = list(combinations(chick, m))



for curjohab in johab:
    total = 0
    for h in home:
        min_dist =987654321
        for chicken in curjohab:
            dist = abs(h[0]-chicken[0]) + abs(h[1]- chicken[1])
            min_dist =min(dist, min_dist)
        
        total+=min_dist
    
    answer= min(answer, total)
        
print(answer)