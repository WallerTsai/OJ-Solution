from collections import deque
from typing import List
from string import ascii_lowercase

# 图论BFS经典应用题目

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        dq = deque([(beginWord, 1)])    
        visited = set([beginWord])
        m = len(beginWord)

        while dq:
            cur_word, level = dq.popleft()

            if cur_word == endWord:
                return level
            
            for i in range(m):
                for ch in ascii_lowercase:
                    nx_word = cur_word[:i] + ch + cur_word[i + 1:]
                    if nx_word in word_set and nx_word not in visited:
                        visited.add(nx_word)
                        dq.append((nx_word, level + 1))

        return 0    # 294ms


class Solution:
    # 双向bfs
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # 使用 Set 代替 Queue，方便判断交集
        begin_set = {beginWord}
        end_set = {endWord}
        visited = {beginWord, endWord}

        m = len(beginWord)
        step = 1

        while begin_set and end_set:
            # 优化： 总是扩展较小的集合
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            nx_set = set()

            for word in begin_set:
                for i in range(m):
                    for ch in ascii_lowercase:
                        nx_word = word[:i] + ch + word[i + 1: ]
                        if nx_word in end_set:
                            return step + 1
                        
                        if nx_word in word_set and nx_word not in visited:
                            visited.add(nx_word)
                            nx_set.add(nx_word)
            
            begin_set = nx_set
            step += 1

        return 0    # 35ms




Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
