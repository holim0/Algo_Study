from collections import defaultdict

# Trie 자료구조안에 위치하고 있는 노드 정의
class Node(object):
    def __init__(self, key, passnumber=None, isEnd=None):
        self.key = key
        # 해당 노드를 지나간 길이 별 단어 갯수
        self.passnumber = {}
        self.isEnd = False
        self.children = {}

# Trie 자료구조
class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 새로운 단어 추가
    def insert(self, string):
        curr_node = self.head
        string_size = len(string)
        if string_size in curr_node.passnumber:
            curr_node.passnumber[string_size] += 1
        else:
            curr_node.passnumber[string_size] = 1
            
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            
            if string_size in curr_node.passnumber:
                curr_node.passnumber[string_size] += 1
            else:
                curr_node.passnumber[string_size] = 1
            

        curr_node.isEnd = True

    # 쿼리 단어에 일치하는 단어 수 반환
    def search(self, query):
        curr_node = self.head
        for q in query:
            if q == "?":
                break
            if q in curr_node.children:
                curr_node = curr_node.children[q]
            else:
                return 0
        if len(query) in curr_node.passnumber:
            return curr_node.passnumber[len(query)]
        else:
            return 0


def solution(words, queries):
    trie = Trie()
     # "?"가 앞에 있는 단어들을 뒤에서 부터 검사하기 위한 r_trie
    r_trie = Trie()
    # 단어 reverse
    r_words = [w[::-1] for w in words]
    # 중복되는 쿼리를 담기 위한 딕셔너리
    dic = {}
    answer = []

    for word in words:
        trie.insert(word)
    for word in r_words:
        r_trie.insert(word)
    for query in queries:
        
        if query.endswith("?"):
            result = trie.search(query)
            answer.append(result)
            dic[query] = result

        else:
            result = r_trie.search(query[::-1])
            answer.append(result)
            dic[query] = result

    return answer