from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums.sort()
        n = len(nums)
        ans = left = right = 0
        for num in sorted(cnt.keys()):
            while nums[left] < num - k:
                left += 1
            while right < n and nums[right] <= num + k:
                right += 1
            ans = max(ans, cnt[num] + min(numOperations, right - left - cnt[num]))
        return ans  # 错误 输入：[88,53] 27 2 输出：1 预期：2
    

class Solution:
    # 不定长滑动窗口
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums.sort()
        n = len(nums)
        ans = left = right = 0
        for num in range(nums[0], nums[-1] + 1):    # 注意这里的遍历区间
            while nums[left] < num - k:
                left += 1
            while right < n and nums[right] <= num + k:
                right += 1
            ans = max(ans, min(numOperations + cnt[num], right - left))
        return ans  # 471ms

class Solution:
    # 差分
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        d = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            d[num] += 0 # 这里很关键，下面遍历需要用到
            d[num - k] += 1
            d[num + k + 1] -= 1

        ans = count = 0
        for num, f in sorted(d.items()):
            count += f  # 解差分
            ans = max(ans, min(cnt[num] + numOperations, count))
        
        return ans  # 1097ms
    
class Solution:
    # 排序 + 二分
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        cnt = Counter(nums)
        
        for x in range(nums[0], nums[-1] + 1):
            l = bisect_left(nums, x - k)
            r = bisect_right(nums, x + k)
            ans = max(ans, min(r - l, numOperations + cnt[x]))
        
        return ans  # 737ms


class Solution:
    # 前缀和
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        MN, MX = min(nums), max(nums)

        cnt = [0] * (MX + 1)
        for num in nums:
            cnt[num] += 1

        prefix = [0] * (MX + 2)     # 这里再 + 1 是为了后面查询方便， 不用特判
        for i, f in enumerate(cnt):
            prefix[i + 1] = prefix[i] + f

        ans = 0
        for num in range(MN, MX + 1):
            count = prefix[min(MX + 1, num + k + 1)] - prefix[max(0, num - k)]
            ans = max(ans, min(count, cnt[num] + numOperations))

        return ans  # 363ms