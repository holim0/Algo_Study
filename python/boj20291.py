import sys
n = int(input())

dict ={}


while n>0:

    name= sys.stdin.readline()


    to_split = name.split(".")

    
    cur = to_split[1]
    if cur not in dict:
        
        dict[cur] = 1

    else:
        dict[cur]+=1

    n-=1


sorted_dict = sorted(dict.items(), key=lambda x: x[0])

for i in range(len(sorted_dict)):
    name, cnt = sorted_dict[i]
    name = name.rstrip("\n")
    print(name, end=" ")
    print(cnt)