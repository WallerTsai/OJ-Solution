from collections import defaultdict
from typing import List


fmax = lambda a, b: a if a >= b else b
class Solution:
    # DP
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 1
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j][d] + 1
                ans = fmax(ans, dp[i][d])
        return ans + 1  # 2217ms
    

class Solution:
    # lc 最快
    def longestArithSeqLength(self, nums: List[int]) -> int:
        def helper(nums, difference):
            dp = defaultdict(int)
            for n in nums:
                dp[n] = dp[n-difference] + 1
            return max(dp.values())
        
        rang = max(nums) - min(nums)
        res = helper(nums, 0)
        i = 1

        while i <= rang // res:
            res = max(helper(nums, i), helper(nums, -i), res)
            i += 1
        
        return res  # 87ms

class Solution:
# 作者：杰
# 链接：https://leetcode.cn/problems/longest-arithmetic-subsequence/solutions/3750472/ling-cha-dai-ma-zao-ting-ji-qiao-jiang-y-sqs9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 2
        m = max(nums)
        n = min(nums)
        d_max = (m-n) // ans
        d = 0
        while d <= d_max:
            f = [0] * (m - n + 1)
            for x in nums:
                f[x-n] = f[x - d - n] + 1 if n <= x - d <= m else 1
            ans = max(ans, max(f))

            f = [0] * (m - n + 1)
            for x in nums:
                f[x-n] = f[x + d - n] + 1 if n <= x + d <= m else 1
            ans = max(ans, max(f))

            d += 1
            d_max = (m-n) // ans
            
        return ans