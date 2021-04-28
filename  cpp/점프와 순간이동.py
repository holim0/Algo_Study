def solution(n):
    ans = 0

    while True:

        if n == 1:
            ans += 1
            break

        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            n /= 2
            ans += 1

    return ans
