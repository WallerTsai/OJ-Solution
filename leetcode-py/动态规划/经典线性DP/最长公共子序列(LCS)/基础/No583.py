class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, ch1 in enumerate(word1):
            for j, ch2 in enumerate(word2):
                if ch1 == ch2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        res = dp[-1][-1]
        return m + n - 2 * res
    

class Solution:
    # leetcode 大佬
    def minDistance(self, word1: str, word2: str) -> int:
        text1=word1
        text2=word2
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        # 构建字符位置掩码
        char_masks = {}
        for i, ch in enumerate(text1):
            char_masks[ch] = char_masks.get(ch, 0) | (1 << i)

        v = 0
        for ch in text2:
            mask = char_masks.get(ch, 0)  # 局部变量，减少字典查找开销
            x = mask | v
            sub = (v << 1) | 1           # 预计算减法中的借位种子
            v = x & (x ^ (x - sub))

        return len(text1) + len(text2)-(v.bit_count()*2)