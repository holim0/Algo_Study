class Node:

    def __init__(self):
        self.children = {}
        self.isEnd = False



class Trie:

    def __init__(self):
        self.root= Node()

    
    def insert(self, word):
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()

            cur = cur.children[w]
        

        cur.isEnd = True
    

    def search(self, word):
        cur = self.root 


        for w in word:
            if w not in cur.children:
                return False

            cur = cur.children[w]

        return cur.isEnd == True
    


tree = {}
total = 0
trie = Trie()
answer = []
while True:
    try:
        N=input().rstrip()
        total+=1
        if trie.search(N):
            tree[N]+=1
        else:
            trie.insert(N)
            if N not in tree:
                tree[N]= 1
            else:
                tree[N]+=1

    except EOFError:
        break


for key, value in tree.items():
    ratio = format(value*100/total, ".4f")
    answer.append((key, ratio))


answer.sort(key = lambda x : x[0])

for name, r in answer:
    print(name, r)





