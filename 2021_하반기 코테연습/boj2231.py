n = int(input())

str_n = str(n)

def Cal(n):

    n = str(n)
    s=0
    for i in n:
        s+=int(i)

    return s+int(n)

isDone = False
for i in range(n-(9*len(str_n)), n):
    if Cal(i)==n:
        print(i)
        isDone=True
        break

if not isDone:
    print(0)