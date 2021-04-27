n = int(input())


def isSosu(number):

    if number == 1:
        return False
    for i in range(2, number):
        if number%i ==0:
            return False
    
    return True





start = n
while True:

    to_string = str(start)

    reverse = to_string[::-1]
    
    if to_string == reverse:
        if isSosu(start):
            print(start)
            break


    start+=1



    
    


