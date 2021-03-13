from datetime import datetime, timedelta


def solution(lines):
    answer = 0
    size = len(lines)
    arr = []

    time_arr = []
    start_time_arr = []

    for i in range(len(lines)):
        tmp = lines[i].split(" ")
        arr.append(tmp)

    sec = arr[0][1].split(".")
    sec = sec[0]
    lower = arr[0][0]+" " + sec
    lower = datetime.strptime(lower, '%Y-%m-%d %H:%M:%S')

    sec = arr[-1][1].split(".")
    sec = sec[0]
    upper = arr[-1][0]+" "+sec
    upper = datetime.strptime(upper, '%Y-%m-%d %H:%M:%S')

    for i in range(size):
        tmp_time = arr[i][0]+" "+arr[i][1]
        end_time = datetime.strptime(tmp_time, '%Y-%m-%d %H:%M:%S.%f')
        gap = arr[i][2].replace("s", "")
        gap = gap.split(".")
        gap_second = int(gap[0])
        gap_milli = 0
        if len(gap) == 2:
            gap_milli = int(gap[1])
        start_time = end_time - \
            timedelta(seconds=gap_second, milliseconds=gap_milli)
        start_time += timedelta(milliseconds=1)
        start_time_arr.append(start_time)
        start_time_arr.append(end_time)
        time_arr.append((start_time, end_time))

    s = lower

    for i in range(len(start_time_arr)):
        start, end = start_time_arr[i], start_time_arr[i] + \
            timedelta(seconds=1)
        tmp_cnt = 0

        for j in range(len(time_arr)):
            s, e = time_arr[j]

            if start <= s < end or start <= e <= end:
                tmp_cnt += 1

            elif s < start and e > end:
                tmp_cnt += 1

        answer = max(answer, tmp_cnt)

    return answer
