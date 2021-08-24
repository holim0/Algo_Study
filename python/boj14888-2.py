n = int(input())

number = list(map(int, input().split()))

oper  = list(map(int, input().split()))

max_answer = -10000000000
min_answer = 10000000000

def getSol(cur_value, idx, plus, minus, mul, div):
    global n, max_answer, min_answer

    if idx == n:
        max_answer = max(max_answer, cur_value)
        min_answer = min(min_answer, cur_value)
        return


    if plus>0:
        getSol(cur_value + number[idx], idx+1, plus-1, minus, mul, div)

    if minus>0:
        getSol(cur_value - number[idx], idx+1, plus, minus-1, mul, div)
    
    if mul>0:
        getSol(cur_value * number[idx], idx+1, plus, minus, mul-1, div)

    if div>0:
        next_val = 0
        if cur_value<0:
            cur_value *= (-1)
            next_val = cur_value // number[idx]
            next_val *= (-1)
        else:
            next_val = cur_value // number[idx]

        getSol(next_val, idx+1, plus, minus, mul, div-1)







if __name__ == '__main__':
    getSol(number[0], 1, oper[0], oper[1], oper[2], oper[3])
    
    print(max_answer)
    print(min_answer)