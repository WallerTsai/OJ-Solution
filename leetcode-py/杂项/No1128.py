from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for d in dominoes:
            d = tuple(sorted(d))  # 只有两个数，排序是 O(1) 的
            ans += cnt[d]
            cnt[d] += 1
        return ans