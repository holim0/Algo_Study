from itertools import combinations

answer= 987654321

n = int(input())


mapp = []
team = []

for i in range(1, n+1):
    team.append(i)


for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)



for i in range(1, n//2+1):
    
    johab = list(combinations(team, i))
    
    for j in johab:
        start = list(j) 
        link = []
        for t in team:
            if t not in start:
                link.append(t)

        start_sum = 0

        link_sum = 0
        
        for a in start:
            for b in start:
                start_sum+= mapp[a-1][b-1]
        
        for a in link:
            for b in link:
                link_sum+= mapp[a-1][b-1]
        
        answer= min(answer, abs(start_sum-link_sum))


print(answer)
