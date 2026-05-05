from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10 **9 + 7
        ans = 0

        nums = [0] + nums + [0]
        n = len(nums)

        pre_sum = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + x

        st = []
        for right,  x in enumerate(nums):
            while st and nums[st[-1]] > x:
                cur_idx = st.pop()
                cur_min = nums[cur_idx]
                left = st[-1]

                # length = right - left - 1
                cur_sum = pre_sum[right] - pre_sum[left + 1]
                ans = max(ans, cur_min * cur_sum)
            st.append(right)

        return ans % MOD




