keyboard = [
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s","d", "f", "g", "h", "j", "k", "l"],
    ["z", "x", "c", "v", "b", "n", "m"]
]

left = ["q", "w", "e", "r", "t","a", "s","d", "f", "g", "z", "x", "c", "v"]


l, r = input().split()
time = 0
string = input()

def find_idx(s):

    for i in range(len(keyboard)):
        cur = keyboard[i]

        for j in range(len(cur)):
            if keyboard[i][j]==s:
                return (i, j)

left_x, left_y = find_idx(l) 
right_x, right_y  = find_idx(r)

for s in string:

    if s in left:
        x, y = find_idx(s)
        
        time+= abs(left_x-x)+abs(left_y-y)+1
        
        left_x, left_y = x, y
    else:
        x, y = find_idx(s)
        time+= abs(right_x-x)+abs(right_y-y)+1
        right_x, right_y = x, y









print(time)