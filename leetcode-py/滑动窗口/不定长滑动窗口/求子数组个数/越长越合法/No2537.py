from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        res = 0
        count = 0
        left = 0
        for right,num in enumerate(nums):
            count += cnt.get(num,0)
            cnt[num] += 1
            while count >= k:
                cnt[nums[left]] -= 1
                count -= cnt[nums[left]]
                left += 1
            res += left
        return res  # 200ms


