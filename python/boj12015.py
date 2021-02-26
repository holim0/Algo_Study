n = int(input())

number = list(map(int, input().split()))

size = len(number)

list = []

list.append(number[0])


for i in range(1, size):

    if list[-1] < number[i]:
        list.append(number[i])
    else:

        l, r = 0, len(list)-1
        changeValue = 0
        while l < r:
            mid = (l+r)//2
            if list[mid] < number[i]:
                l = mid+1

            elif list[mid] > number[i]:
                r = mid
            else:
                l = r = mid

        list[r] = number[i]

print(len(list))
