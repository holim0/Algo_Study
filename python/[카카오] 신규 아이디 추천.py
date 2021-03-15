import copy


def change(new_id):

    size = len(new_id)
    new_id = new_id.lower()

    new_id = list(new_id)

    for i in range(size):

        if new_id[i].isalpha():
            continue

        if new_id[i].isdigit():
            continue

        if new_id[i] == "-" or new_id[i] == "_" or new_id[i] == ".":
            continue

        new_id[i] = " "

    new_id = "".join(new_id)
    new_id = new_id.replace(" ", "")

    tmp_id = ""

    for i in range(len(new_id)):

        if len(tmp_id) > 0 and new_id[i] == "." and tmp_id[-1] == ".":
            continue

        tmp_id += new_id[i]

    new_id = tmp_id
    new_id = list(new_id)

    if new_id[0] == ".":
        new_id[0] = ""

    if new_id[-1] == ".":
        new_id[-1] = ""

    new_id = "".join(new_id)

    if len(new_id) == 0:
        new_id += "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:len(new_id)-1]

    if len(new_id) <= 2:

        plus_char = new_id[-1]

        gap = 3-len(new_id)

        while gap:
            new_id += plus_char
            gap -= 1

    return new_id


def solution(new_id):
    answer = ''

    answer = change(new_id)

    return answer
