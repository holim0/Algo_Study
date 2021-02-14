import sys
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())

flag = False

sum_val = a+b+c


def dfs(a, b, check):
    global flag, sum_val

    if check[a][b]:
        return
    check[a][b] = True

    num_list = [a, b, sum_val-a-b]

    for i in range(3):
        for j in range(i + 1, 3):
            if num_list[i] < num_list[j]:
                tmp_a = 2*(num_list[i])
                tmp_b = num_list[j] - num_list[i]

                dfs(tmp_a, tmp_b, check)
            else:
                tmp_a = num_list[i] - num_list[j]
                tmp_b = 2*(num_list[j])

                dfs(tmp_a, tmp_b, check)


if __name__ == '__main__':

    check = [[False] * 1505 for _ in range(1505)]

    if (a+b+c) % 3 != 0:
        print(0)
    else:

        dfs(a, b, check)

        if check[sum_val//3][sum_val//3]:
            print(1)
        else:
            print(0)
