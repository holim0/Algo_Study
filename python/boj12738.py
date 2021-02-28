n = int(input())

number = list(map(int, input().split()))

number_size = len(number)
list = []

list.append(number[0])


for i in range(1, number_size):

    cur = number[i]

    if cur > list[-1]:
        list.append(cur)
    else:
        l, r = 0, len(list)-1

        while l < r:

            mid = (l+r)//2

            if list[mid] < cur:
                l = mid+1
            elif list[mid] > cur:
                r = mid

            else:
                l = r = mid

        list[r] = cur


print(len(list))
