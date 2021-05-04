from itertools import permutations
n = int(input())

answer =0

digit= ["1", "2", "3", "4", "5", "6", "7", "8","9"]



johab = list(permutations(digit, 3))
talk =[]

def check_answer(n, target_n, t_strike, t_ball):

    cur_strike, cur_ball=0, 0


    for i in range(3):
        for j in range(3):

            if i==j and n[i] == target_n[j]:
                cur_strike+=1

            elif i!=j and n[i] == target_n[j]:
                cur_ball+=1



    if cur_strike== t_strike and cur_ball == t_ball:
        return True
    else:
        return False


while n>0:

    number, strike, ball = map(int, input().split())

    talk.append((number, strike, ball))
    
    n-=1

for j in johab:
    to_str = "".join(j)
    isAnswer = True
    for t in talk:
        number, strike, ball = t
        if not check_answer(to_str, str(number), strike, ball):
            isAnswer = False
            break
    
    if isAnswer : answer+=1







print(answer)