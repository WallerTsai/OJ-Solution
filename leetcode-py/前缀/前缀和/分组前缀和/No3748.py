from bisect import bisect_right
from typing import List


class Solution:
    # 灵神
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        segment_left = [] # 递增段的左端点
        pre_nums = [0] # 递增段的个数前缀和
        start = 0
        for i, num in enumerate(nums):
            if i == n - 1 or num > nums[i + 1]:
                segment_left.append(start)
                m = i - start + 1
                pre_nums.append(pre_nums[-1] + m * (m + 1) // 2)
                start = i + 1

        ans = []
        for l, r in queries:
            l_idx = bisect_right(segment_left, l)
            r_idx = bisect_right(segment_left, r) - 1

            # l_idx 和 r_idx 在同一段上
            if l_idx > r_idx:
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
                continue

            # l_idx 和 r_idx 在不同区间
            # 分三段 [l, left[l_idx]] + pre_nums[r_idx] - pre_nums[l_idx] + [left[r_idx], right]

            m1 = segment_left[l_idx] - l
            m2 = r - segment_left[r_idx] + 1
            ans.append(m1 * (m1 + 1) // 2 + pre_nums[r_idx] - pre_nums[l_idx] + m2 * (m2 + 1) // 2)

        return ans