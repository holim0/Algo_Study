n, m = map(int, input().split())

S = []
target =[]

for _ in range(n):
    tmp = input()
    S.append(tmp)


for _ in range(m):
    tmp = input()
    target.append(tmp)

class Trie:
    
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root

        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        
        cur["*"] = True
    

    def check_match(self, word):
        cur = self.root

        for w in word:
            if w not in cur: 
                return False

            cur = cur[w]
        
        return "*" in cur


answer = 0

trie = Trie()

for s in S:
    trie.insert(s)

for t in target:

    if trie.check_match(t):
        answer+=1


print(answer)