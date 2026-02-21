from collections import Counter
from itertools import pairwise
from typing import List


class Solution:
    # 手写比较函数
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def compare(s1: str, s2: str) -> bool:
            cnt = [0] * 26
            for ch in s1:
                cnt[ord(ch) - ord('a')] += 1
            for ch in s2:
                cnt[ord(ch) - ord('a')] -= 1
            return all(x == 0 for x in cnt)
        
        res = [words[0]]
        for i in range(1, len(words)):
            if compare(words[i], words[i - 1]):
                continue
            res.append(words[i])
        return res  # 27ms
    

class Solution:
    # 灵神
    def removeAnagrams(self, words: List[str]) -> List[str]:
        k = 1
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):
                words[k] = t
                k += 1
        return words[:k]    # 4ms
    
class Solution:
    # wxyz
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # 初始化一个栈，并将第一个单词放进去
        stack = [words[0]]

        for i in range(1, len(words)):
            # 检查与前一个单词，是否组成相同
            if Counter(words[i]) != Counter(stack[-1]):
                stack.append(words[i])
        
        return stack    # 39ms

