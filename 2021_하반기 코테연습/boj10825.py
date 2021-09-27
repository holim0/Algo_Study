n = int(input())

info = []

for _ in range(n):
    tmp = list(input().split())

    tmp[1], tmp[2], tmp[3] = int(tmp[1]), int(tmp[2]), int(tmp[3])

    info.append(tmp)



sorted_info = sorted(info, key= lambda x:(-x[1], x[2], -x[3], x[0]))




for i in sorted_info:
    print(i[0])
