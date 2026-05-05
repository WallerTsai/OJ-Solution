class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    # 更新单点最大值
    def update(self, i, val):
        while i < len(self.tree):
            if val > self.tree[i]:
                self.tree[i] = val
            i += i & -i
            
    # 查询前缀最大值
    def query(self, i):
        res = 0
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & -i
        return res
    
class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)

        dp = [[0, 0] for _ in range(n)]
        inc = BIT(mx)  # 维护 f_inc[i] 的最大值
        dec = BIT(mx)  # 维护 f_dec[i] 的最大值

        ans = 0

        for i, x in enumerate(nums):
            if i >= k:
                pre = nums[i - k]
                inc.update(pre, dp[i - k][0])
                dec.update(mx - pre + 1, dp[i - k][1])

            dp[i][0] = x + dec.query(mx - x)
            dp[i][1] = x + inc.query(x - 1)

            ans = max(ans, dp[i][0], dp[i][1])

        return ans
                


