from itertools import permutations
import re


def calFun(n1, n2, oper):

    if oper == "+":
        return n1+n2
    elif oper == "-":
        return n1-n2
    else:
        return n1*n2


def solution(expression):
    answer = 0

    # 실제 연산자
    oper = []

    for c in expression:
        if c.isdigit() == False:
            oper.append(c)

    real_oper = set(oper)

    size = len(real_oper)
    johab = list(permutations(real_oper, size))

    num_list = re.findall("\d+", expression)

    for cur_johab in johab:
        tmp_num = num_list.copy()
        tmp_oper = oper.copy()
        for o in cur_johab:
            for val in oper:
                if o == val:
                    idx = tmp_oper.index(val)
                    result = calFun(int(tmp_num[idx]), int(
                        tmp_num[idx+1]), tmp_oper[idx])
                    tmp_oper.pop(idx)
                    tmp_num.pop(idx)
                    tmp_num.pop(idx)
                    tmp_num.insert(idx, result)

                if len(tmp_oper) == 1:
                    val = calFun(int(tmp_num[0]), int(tmp_num[1]), tmp_oper[0])
                    answer = max(answer, abs(val))
                    break

    return answer
