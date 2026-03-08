from math import inf
from typing import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        ans = [inf, inf]
        for i, x in cnt.items():
            if i < ans[0] and cnt[ans[0]] == x:
                ans[0] = i
            elif i < ans[0] and cnt[ans[0]] != x:
                ans[0], ans[1] = i, ans[0]
            elif i < ans[1] and cnt[ans[0]] != x:
                ans[1] = i

            if ans[0] > ans[1]:
                ans[0], ans[1] = ans[1], ans[0]

        return ans if ans[0] != inf and ans[1] != inf else [-1, -1]


Solution().minDistinctFreqPair([1,1,2,2,3,4])       
            