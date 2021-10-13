n = int(input())


def pac(cur):

    if cur==1:
        return cur
    
    return cur * pac(cur-1)

    


if n==0:
    print(1)
else:
    print(pac(n))