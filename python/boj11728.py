n, m = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer=[]

ap = 0
bp = 0

while ap<len(a) and bp<len(b):

    
    if a[ap] > b[bp]:
        
        answer.append(b[bp])
        bp+=1
    
    else:
        
        answer.append(a[ap])
        ap+=1

if ap<len(a):
    while ap<len(a):
        answer.append(a[ap])
        ap+=1

if bp<len(b):

    while bp<len(b):
        answer.append(b[bp])
        bp+=1

for ans in answer:
    print(ans, end=" ")