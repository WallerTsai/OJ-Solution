from math import inf
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 处理所有子集和
        m = 1 << len(cookies)
        SUM = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                SUM[bit | j] = SUM[j] + v

        # 定义 f[i][j] 表示前 i 个孩子分配的饼干集合为 j 时，前 i 个孩子的不公平程度的最小值
        # f 第一个维度可以忽略
        dp = SUM.copy()

        for _ in range(1, k):
            for j in range(m - 1, 0, -1):
                s = j   # s 为当前分配这个孩子的饼干, j 为饼干集合
                while s:
                    # Min-Max
                    v = dp[j ^ s]
                    if SUM[s] > v:
                        v = SUM[s]
                    if v < dp[j]:
                        dp[j] = v
                    # 高效遍历 s 子集
                    s = (s - 1) & j
        
        return dp[-1]


# 理解版本
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 处理所有子集和
        m = 1 << len(cookies)
        SUM = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                SUM[bit | j] = SUM[j] + v

        # 定义 f[i][j] 表示前 i 个孩子分配的饼干集合为 j 时，前 i 个孩子的不公平程度的最小值
        # 如果 sum[s]>f[i−1][j∖s]，说明给第 i 个孩子分配的饼干比前面的孩子多，不公平程度变为 sum[s]；
        # 如果 sum[s]≤f[i−1][j∖s]，说明给第 i 个孩子分配的饼干没有比前面的孩子多，不公平程度不变，仍为 f[i−1][j∖s]。
        dp = [[inf] * m for _ in range(k + 1)]
        dp[0][0] = 0
        
        for i in range(1, k + 1):   # 孩子数量
            for j in range(1, m):   # 饼干状态
                s = j   # s 为 j 的子集，分配给第 i 个孩子的饼干
                while s:
                    cur_max = max(SUM[s], dp[i - 1][j ^ s])
                    dp[i][j] = min(dp[i][j], cur_max)
                    # 高效枚举子集
                    s = (s - 1) & j
        
        return dp[k][m - 1]