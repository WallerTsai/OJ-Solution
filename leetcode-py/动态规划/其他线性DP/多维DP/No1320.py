from functools import cache
from itertools import pairwise

# 预处理两个字母的距离
COLUMN = 6
get_dis = lambda a, b: abs(a // COLUMN - b // COLUMN) + abs(a % COLUMN - b % COLUMN)
dis = [[get_dis(i, j) for j in range(26)] for i in range(26)]

class Solution:
    def minimumDistance(self, word: str) -> int:
        word = [ord(ch) - ord('A') for ch in word]

        @cache
        def dfs(i: int, another_finger: int):
            if i < 0:
                return 0
            
            # 另外一个手指不动, 第一根手指移动到 words[i + 1]
            res1 = dfs(i - 1, another_finger) + dis[word[i + 1]][word[i]]
            # 另外一个手指动， 移动到 words[i + 1]
            res2 = dfs(i - 1, word[i + 1]) + dis[another_finger][word[i]]

            return min(res1, res2)

        n = len(word)
        ans = min(dfs(n - 2, another_finger) for another_finger in range(26))
        dfs.cache_clear()

        return ans
    

# 预处理两个字母的距离
COLUMN = 6
get_dis = lambda a, b: abs(a // COLUMN - b // COLUMN) + abs(a % COLUMN - b % COLUMN)
dis = [[get_dis(i, j) for j in range(26)] for i in range(26)]

class Solution:
    def minimumDistance(self, word: str) -> int:
        f = [[0] * 26 for _ in word]
        for i, (x, y) in enumerate(pairwise(word)):
            x = ord(x) - ord('A')
            y = ord(y) - ord('A')
            for another_finger in range(26):
                f[i + 1][another_finger] = min(f[i][another_finger] + dis[y][x], f[i][y] + dis[another_finger][x])
        return min(f[-1])






