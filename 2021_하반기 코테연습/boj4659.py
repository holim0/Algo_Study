mo = ["a", "e", "i", "o", "u"]
def check_mo(password):

    global mo

    for p in password:
        if p in mo : return True

    return False

def check_succession(password):
    global mo
    
    for i in range(len(password)-2):
        mo_cnt, ja_cnt= 0, 0
        for j in range(i, i+3):
            if password[j] in mo:
                mo_cnt+=1
            else:
                ja_cnt+=1
        
        if mo_cnt==3 or ja_cnt==3:
            return True
    
    return False

def check_double(password):

    for i in range(len(password)-1):

        if password[i]==password[i+1]:
            if password[i]=="e" or password[i]=="o": continue
            else:
                return True

    return False





while True:

    
    password = input()
    if password=="end": break


    if check_mo(password) and not check_succession(password) and not check_double(password):
        print("<{a}> is acceptable.".format(a=password))

    else:
        print("<{a}> is not acceptable.".format(a=password))
