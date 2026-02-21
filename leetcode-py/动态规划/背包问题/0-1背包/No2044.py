from collections import defaultdict
import collections
from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums)
        def dfs(i: int, cur: int):
            if i == n:
                cnt[cur] += 1
                return
            dfs(i + 1, cur | nums[i])
            dfs(i + 1, cur)
        dfs(0,0)
        return cnt[max(cnt.keys())]
    
class Solution:
    # 根据or性质 参与or的元素越多 结果越大
    # 灵神
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        total_or = reduce(or_, nums)
        n = len(nums)
        ans = 0

        def dfs(i: int, subset_or: int) -> None:
            if i == n:
                if subset_or == total_or:
                    nonlocal ans
                    ans += 1
                return
            dfs(i + 1, subset_or) # 不选 nums[i]
            dfs(i + 1, subset_or | nums[i])  # 选 nums[i]

        dfs(0, 0)
        return ans
    
class Solution:
    # leetcode 大佬
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        for num in nums:
            for k, v in dp.copy().items():
                dp[k | num] += v
        return dp[max(dp)]