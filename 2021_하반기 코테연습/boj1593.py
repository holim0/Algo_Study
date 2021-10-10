from collections import deque, Counter
g, s_len = map(int, input().split())

w = input()
S = input()

cnt_w = [0 for _ in range(100)]
cnt_s = [0 for _ in range(100)]


answer = 0
for ww in w:
    cnt_w[ord(ww)-65]+=1

for i in range(g):
    cur = ord(S[i])-65
    cnt_s[cur]+=1


for i in range(s_len-g+1):
    if i==0:
        if cnt_w==cnt_s:
            answer+=1
    else:
        cnt_s[ord(S[i-1])-65]-=1
        cnt_s[ord(S[i+g-1])-65]+=1
        
        if cnt_w==cnt_s:
            answer+=1
        

print(answer)