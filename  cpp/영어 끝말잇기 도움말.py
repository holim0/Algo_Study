def solution(n, words):
    answer = []

    dic = {}

    for word in words:
        dic[word] = False

    for i in range(0, len(words)):

        if i != 0:
            pre = words[i-1][len(words[i-1])-1]
            cur = words[i][0]
            if pre != cur:
                if (i+1) % n == 0:
                    answer.append(n)
                    answer.append((i+1)/n)
                    break
                else:
                    answer.append((i+1) % n)
                    answer.append(int((i+1)/n)+1)
                    break

        if dic[words[i]] == False:
            dic[words[i]] = True
        else:
            if (i+1) % n == 0:
                answer.append(n)
                answer.append((i+1)/n)
                break
            else:
                answer.append((i+1) % n)
                answer.append(int((i+1)/n)+1)
                break

    if len(answer) == 0:
        answer.append(0)
        answer.append(0)

    return answer
