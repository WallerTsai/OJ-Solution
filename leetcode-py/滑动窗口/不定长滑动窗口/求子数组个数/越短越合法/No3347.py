from collections import defaultdict
from typing import List


class Solution:
    # 差分
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        d = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            d[num] # 这里很关键，下面遍历需要用到
            d[num - k] += 1
            d[num + k + 1] -= 1

        ans = count = 0
        for num, f in sorted(d.items()):
            count += f  # 解差分
            ans = max(ans, min(cnt[num] + numOperations, count))
        
        return ans  # 1748ms
    
# 由于nums[i] 的范围从 1e5 变为 1e9
# 所以不能遍历range(MN, MX)


class Solution:
    # 灵神
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        # 同向三指针
        n = len(nums)
        ans = cnt = left = right = 0
        for i, x in enumerate(nums):
            cnt += 1
            # 循环直到连续相同段的末尾，这样可以统计出 x 的出现次数
            if i < n - 1 and x == nums[i + 1]:
                continue
            while nums[left] < x - k:
                left += 1
            while right < n and nums[right] <= x + k:
                right += 1
            ans = max(ans, min(right - left, cnt + numOperations))
            cnt = 0

        # 由于同向双指针算出的结果不超过 numOperations，所以当同向三指针计算完毕后，如果发现答案已经 ≥numOperations，那么无需计算同向双指针
        if ans >= numOperations:
            return ans

        # 同向双指针
        left = 0
        for right, x in enumerate(nums):
            while nums[left] < x - k * 2:
                left += 1
            ans = max(ans, right - left + 1)
        return min(ans, numOperations)  # 最后和 numOperations 取最小值
        # 303ms
