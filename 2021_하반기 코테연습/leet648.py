class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        t = self.root
        for w in word:
            if w not in t:
                t[w] ={}        
            t = t[w]
        t["*"] = True
                        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        
        return True
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer = []
        
        split_sentence =  sentence.split(" ")
        dictionary = sorted(dictionary, key = lambda x: len(x))
        
        for s in split_sentence:
            
            trie = Trie()
            trie.insert(s)
            flag = False
            for dict in dictionary:
                if trie.startsWith(dict):
                    answer.append(dict)
                    flag = True
                    break
            
            if flag==False:
                answer.append(s)
    
        
        return " ".join(answer)
        
        
    
    