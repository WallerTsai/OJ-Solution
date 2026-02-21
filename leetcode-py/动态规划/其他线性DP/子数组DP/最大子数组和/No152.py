from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def dfs(i: int):
            if i < 0:
                return 0
            res = nums[i]
            return max(res, res * dfs(i - 1), dfs(i - 1))
        return dfs(len(nums) - 1) # 错误
    

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = nums[0]

        for i in range(1, n):
            num = nums[i]
            dp_max[i] = max(num, dp_max[i - 1] * num, dp_min[i - 1] * num)
            dp_min[i] = min(num, dp_min[i - 1] * num, dp_max[i - 1] * num)

        return max(dp_max)
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        MX = MN = 1
        for num in nums:
            MX, MN = max(num, MX * num, MN * num), min(num, MX * num, MN * num)
            ans = max(ans, MX)
        return ans


class Solution:
    # 灵神
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        f_max = f_min = 1
        for x in nums:
            if x < 0:
                # 下面与 x 相乘后，最大的正数变成最小的负数，最小的负数变成最大的正数
                # 提前交换，这样可以把 x < 0 和 x >= 0 的情况合并，合并后，计算 max 和 min 可以少一项
                f_max, f_min = f_min, f_max
            f_max = max(f_max * x, x)
            f_min = min(f_min * x, x)
            ans = max(ans, f_max)
        return ans

