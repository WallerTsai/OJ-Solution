from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        if s in wordDict:
            return True
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i):
                if s[j: i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]

class Solution:
    # 灵神
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        words = set(wordDict)  # 便于快速判断 s[j:i] in words

        n = len(s)
        f = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if f[j] and s[j:i] in words:
                    f[i] = True
                    break
        return f[n]



