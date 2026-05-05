from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                if sum(x != y for x, y in zip(q, d)) <= 2:
                    res.append(q)
                    break
        return res
    


class Node:
    # 灵神字典树模板
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:  # 无路可走？
                cur.son[c] = Node()  # 那就造路！
            cur = cur.son[c]
        cur.end = True

    def search_with_edits(self, word: str, max_edits: int) -> bool:
        def dfs(node: Node, i: int, edits_left: int) -> bool:
            if i == len(word):
                return node.end
            
            c = word[i]
            if c in node.son and dfs(node.son[c], i + 1, edits_left):
                return True
            
            if edits_left > 0:
                for nx_c, nx_node in node.son.items():
                    if nx_c != c and dfs(nx_node, i + 1, edits_left - 1):
                        return True
            
            return False
        
        return dfs(self.root, 0, max_edits)
    
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        res = []
        for q in queries:
            if trie.search_with_edits(q, 2):
                res.append(q)

        return res