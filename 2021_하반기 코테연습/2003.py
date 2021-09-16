n, m = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0


s,e = 0, 0 

acc = [a[0]]

for i in range(1, n):
    acc.append(acc[i-1]+ a[i])

while e<n:

    val = -1
    
    if s==e:
        if a[s] == m: cnt+=1
        e+=1
        continue

    elif s==0 and e>s:
        val = acc[e]

    elif s>0 and e>0:
        val = acc[e] - acc[s-1]

    
    if val == m: 
        cnt+=1
        
        e+=1
    
    elif val>m:
        s+=1
    elif val<m:
        e+=1
    

print(cnt)