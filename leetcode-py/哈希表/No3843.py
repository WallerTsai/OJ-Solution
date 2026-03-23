from collections import Counter
from typing import  List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt1 = Counter(nums)
        cnt2 = Counter(cnt1.values())

        for x in nums:
            if cnt2[cnt1[x]] == 1:
                return x

        return -1



