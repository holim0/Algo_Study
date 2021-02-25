n = int(input())

answer = 0


if len(str(n)) < 3:
    answer = n
else:
    answer = 99

    for i in range(100, n+1):
        s = str(i)

        if (int(s[0])-int(s[1])) == (int(s[1])-int(s[2])):
            answer += 1

print(answer)
