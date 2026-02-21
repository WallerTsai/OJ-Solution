from collections import defaultdict
from typing import List

# 在子数组递增且包含多种不同元素的情况下，
# 进入窗口的元素一定比离开窗口的元素大，
# 所以这些子数组一定互不相同。
# 所以只有当子数组只包含一种元素时，才会出现相同的子数组。

class Solution:
    # 灵神
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 见 560 题
        pre_sum = 0  # 前缀和
        last_start = 0  # 上一个连续相同段的起始下标
        ans = 0

        for i, x in enumerate(nums):
            if i and x != nums[i - 1]:
                # 上一个连续相同段结束，可以把上一段对应的前缀和添加到 cnt
                v = nums[i - 1]
                s = pre_sum
                for _ in range(i - last_start):
                    cnt[s % k] += 1
                    s -= v
                last_start = i

            pre_sum += x
            ans += cnt[pre_sum % k]

        return ans
    
fun = Solution()
res = fun.numGoodSubarrays([1, 2, 2, 3, 3, 3], 6)
print(res)