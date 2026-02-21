from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(nums)
        cnt = Counter(nums[:k - 1])
        cnt[nums[-1]] += 1
        right = k - 1
        left = -1
        for i in range(n - k + 1):
            cnt[nums[right]] += 1
            cnt[nums[left]] -= 1
            most_common = sorted(cnt.items(), key= lambda x: (-x[1], -x[0]))
            temp = sum(x * y for x, y in most_common[:x])
            ans.append(temp)
            right += 1
            left += 1
        return ans



