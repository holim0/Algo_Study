import math


def solution(n, stations, w):
    answer = 0

    cover = 2*w+1

    for i in range(len(stations)):

        if len(stations) == 1:
            tmp = stations[0]-w-1
            answer += math.ceil(tmp/cover)
            tmp = n-(stations[0]+w+1)+1
            if tmp > 0:
                answer += math.ceil(tmp/cover)
        else:
            if i == 0:
                tmp = stations[i]-w-1
                answer += math.ceil(tmp/cover)
                tmp = (stations[i+1]-w-1)-(stations[i]+w+1)+1
                answer += math.ceil(tmp/cover)

            elif i > 0 and i < len(stations)-1:
                tmp = (stations[i+1]-w-1)-(stations[i]+w+1)+1
                answer += math.ceil(tmp/cover)
            elif i == len(stations)-1:
                tmp = n-(stations[i]+w+1)+1
                if tmp > 0:
                    answer += math.ceil(tmp/cover)

    return answer
