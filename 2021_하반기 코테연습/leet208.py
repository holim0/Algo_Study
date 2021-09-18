class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        t = self.root
        for w in word:
            if w not in t:
                t[w] ={}        
            t = t[w]
        t["*"] = True
                
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        
        return "*" in cur
                
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)