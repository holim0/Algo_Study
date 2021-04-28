import re
n = int(input())

check_alpa= "ABCDEF"

while n>0:

    s = input()

    if re.search("[A-F]?A+F+C+[A-F]?", s):
        tmp= re.search("[A-F]?A+F+C+[A-F]?", s).group()
        if tmp!= s:
            print("Good")
        else:
            print("Infected!")

    else:
        print("Good")

    n-=1