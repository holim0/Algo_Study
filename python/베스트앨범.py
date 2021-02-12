def solution(genres, plays):
    answer = []

    size = len(genres)
    dict = {}

    cnt = {}

    for i in range(size):
        g = genres[i]
        if genres[i] not in dict:
            dict[g] = [[plays[i], i]]
            cnt[g] = plays[i]
        else:
            dict[g].append([plays[i], i])
            cnt[g] += plays[i]

    sorted_cnt = sorted(cnt.items(), key=lambda x: -x[1])

    for key in dict:
        dict[key] = sorted(dict[key], key=lambda x: (-x[0], x[1]))

    for key, value in sorted_cnt:
        if len(dict[key]) > 1:
            answer.append(dict[key][0][1])
            answer.append(dict[key][1][1])
        else:
            answer.append(dict[key][0][1])

    return answer
