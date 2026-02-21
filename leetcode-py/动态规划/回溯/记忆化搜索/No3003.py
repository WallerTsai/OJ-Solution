#  难度 3039
#  无法战胜
from functools import cache


# https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations/solutions/2595072/ji-yi-hua-sou-suo-jian-ji-xie-fa-pythonj-6g5z/

class Solution:
    # cv from 灵神
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, mask: int, changed: bool) -> int:
            if i == len(s):
                return 1

            # 不改 s[i]
            bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | bit
            if new_mask.bit_count() > k:
                # 分割出一个子串，这个子串的最后一个字母在 i-1
                # s[i] 作为下一段的第一个字母，也就是 bit 作为下一段的 mask 的初始值
                res = dfs(i + 1, bit, changed) + 1
            else:  # 不分割
                res = dfs(i + 1, new_mask, changed)
            if changed:
                return res

            # 枚举把 s[i] 改成 a,b,c,...,z
            for j in range(26):
                new_mask = mask | (1 << j)
                if new_mask.bit_count() > k:
                    # 分割出一个子串，这个子串的最后一个字母在 i-1
                    # j 作为下一段的第一个字母，也就是 1<<j 作为下一段的 mask 的初始值
                    res = max(res, dfs(i + 1, 1 << j, True) + 1)
                else:  # 不分割
                    res = max(res, dfs(i + 1, new_mask, True))
            return res

        return dfs(0, 0, False)