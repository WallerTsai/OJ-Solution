from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        word_set = set()
        word_length = len(words)

        for i in range(word_length):
            for j in range(i+1,word_length):
                if words[i] in words[j]:
                    word_set.add(words[i])
        
        return list(word_set)
    
import re
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # 按长度排序
        sorted_words = sorted(words, key=len)
        result = set()
        
        for i in range(len(sorted_words)):
            current_word = sorted_words[i]
            pattern = re.compile(re.escape(current_word))
            
            # 只在更长的单词中搜索
            for j in range(i + 1, len(sorted_words)):
                if pattern.search(sorted_words[j]):
                    result.add(current_word)
                    break
        
        return list(result)