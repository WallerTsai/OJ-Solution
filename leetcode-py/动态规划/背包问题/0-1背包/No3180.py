from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        li = sorted(set(rewardValues))
        dp = {0}

        for v in li:
            nx_dp = { x + v for x in dp if x < v}
            dp |= nx_dp

        return max(dp)


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        li = sorted(set(rewardValues))
        dp = 1
        for v in li:
            mask = (1 << v) - 1
            valid = dp & mask
            dp |= (valid << v)
        return dp.bit_length() - 1