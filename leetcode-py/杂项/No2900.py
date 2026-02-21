from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        res = []
        for i, g in enumerate(groups):
            if i  == n - 1 or g != groups[i + 1]:
                res.append(words[i])
        return res



