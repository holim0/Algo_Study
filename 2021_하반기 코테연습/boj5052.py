t = int(input())


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root

        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
            if "*" in cur:
                return False
    
        cur["*"] = True
        return True


while t:
    n = int(input())
    arr = []
    for i in range(n):
        tmp = input()
        arr.append(tmp)

    trie = Trie()
    
    
    arr.sort()
    answer = []
    for n in arr:
        
        if not trie.insert(n):
            answer.append("No")
            
        else:
            answer.append("Yes")
    flag = False
    for a in answer:
        if a=="No":
            print("NO")
            flag = True
            break

    if flag==False:
        print("YES")
            

    
    

    t-=1
