money = int(input())

price = list(map(int, input().split()))

def jun():

    cur_money = money 
    cnt = 0
    for p in price:
        if cur_money>=p:
            cnt+= cur_money//p
            
            cur_money = cur_money%p

    return cur_money + price[-1] * cnt


def sung():
     
    cur_money = money
    cnt = 0

    for i in range(3, len(price)):
        ## 감소
        if price[i-1]<price[i-2] and price[i-2]<price[i-3]:
            if cur_money>=price[i]:
                cnt+=cur_money//price[i]
                cur_money%=price[i]

        ## 증가 
        elif price[i-1]>price[i-2] and price[i-2]>price[i-3]:
            cur_money+= cnt*price[i]
            cnt =0


    return cur_money+ cnt * price[-1]







junM = jun()
sungM = sung()



if junM>sungM:
    print("BNP")
elif junM<sungM:
    print("TIMING")
else:
    print("SAMESAME")