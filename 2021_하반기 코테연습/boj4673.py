check = [False for _ in range(20000+1)]


cur = 1

for i in range(1, 10001):

    val = i
    
    str_i = str(i)

    for s in str_i:
        val+=int(s)

    check[val] = True

for i in range(1, 10001):
    if not check[i]:
        print(i, end="\n")
