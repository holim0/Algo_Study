import sys

input = sys.stdin.readline

n = int(input())

def ispseudo(s, isFront):
    start, end = 0, len(s)-1
    delete = False
    while start<=end:
        if s[start]==s[end]:
            start+=1
            end-=1
            continue

        if delete and s[start]!=s[end]:
            return False
            break

        if s[start]!=s[end] and not delete:
            if isFront and s[start+1]==s[end]:
                start+=2
                end-=1
                delete=True
            elif not isFront and s[start]==s[end-1]:
                start+=1
                end-=2
                delete=True
            else:
                return False

    return True          


while n:

    s = input()
    s= s.rstrip("\n")
    
    if s==s[::-1]:
        print(0)

    else:
        

        if ispseudo(s, True) or ispseudo(s, False):
            print(1)
        else:
            print(2)
        



    n-=1