from itertools import accumulate
from math import inf
from typing import List


class Solution:
    # f佬
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pres = list(accumulate(nums, initial=0))
        dp = [[inf] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(i, k)+1):  # 优化：减少 j 的枚举范围
                dp[i][j] = min(dp[p][j-1] + (pres[i] - pres[p]) ** 2 for p in range(i))
        return (dp[n][k] + pres[n]) // 2    # 超时
    

import numpy as np
inf = 1 << 60
class Solution:
    # f佬
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pres = np.r_[0, np.cumsum(nums, dtype=np.int64)]
        dp = np.full((k+1, n+1), inf, dtype=np.int64)  # 注意这里和下文都交换了 n 和 k 的维度
        dp[0, 0] = 0
        for i in range(1, n+1):
            j = min(i, k)
            # 为什么要交换维度？
            # `pres[i] - pres[:i]` 是一个 1D-array
            # 当其与 2D-array 作运算时，会触发 broadcast 机制与 2D-array 的每个行向量作运算
            # 所以要把此前的列向量 `dp[:i, j-1]` 转置为行向量 `dp[j-1, :i]`
            # 再对 i 所在维度向量化即有 `dp[:j, :i]`
            # 注意：`dp[:j, :i]` 子矩阵里包含了一些无效状态，必须初始化为 `inf`
            dp[1:j+1, i] = np.min(dp[:j, :i] + (pres[i] - pres[:i]) ** 2, axis=1)
        return (dp[k, n] + pres[n]).item() // 2

