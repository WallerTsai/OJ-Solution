from typing import List


class Solution:
    # 01背包 + bitset优化
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        li = sorted(set(rewardValues))
        dp = 1
        for v in li:
            mask = (1 << v) - 1
            valid = dp & mask
            dp |= (valid << v)
        return dp.bit_length() - 1