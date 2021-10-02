n = int(input())

tri = []


for _ in range(n):

    tmp = list(map(int, input().split()))
    tri.append(tmp)



for i in range(1, n):
    for j in range(len(tri[i])):
    
        if j==0:
            tri[i][j] +=tri[i-1][j]

        elif j==len(tri[i])-1:
            tri[i][j] += tri[i-1][-1]

        else:
            max_val = max(tri[i-1][j-1], tri[i-1][j])
            tri[i][j]+=max_val


print(max(tri[n-1]))