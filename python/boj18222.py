k = int(input())

num = [-1, 0, 1]

reverse ={
    0: 1,
    1: 0
}

cnt =0

def find_location(n):

    i=0

    while True:

        if 2**i < n and n<=2**(i+1):
            return n-2**i
        
        i+=1

while True:

    if k==1 or k==2:
        if cnt%2==0:
            print(num[k])
        else:
            print(reverse[num[k]])
        
        break

    k = find_location(k)
    cnt+=1
