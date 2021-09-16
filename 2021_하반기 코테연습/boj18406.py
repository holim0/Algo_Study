n = int(input())


s = str(n)
s = list(s)
l = s[:len(s)//2]
r = s[len(s)//2:]



l_s = 0
r_s = 0

for i in range(len(s)//2):
    
    l_s+=int(l[i])
    r_s+=int(r[i])


if l_s == r_s:
    print("LUCKY")

else:
    print("READY")


