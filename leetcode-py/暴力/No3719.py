from collections import Counter
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        odd = even = 0
        cnt = {0: -1}
        ans = d = 0
        a_set = set()
        for i, num in enumerate(nums):
            if num not in a_set:
                a_set.add(num)
                if num % 2:
                    d += 1
                    odd = 1
                else:
                    d -= 1
                    even = 1
            if d in cnt:
                ans = max(ans, i - cnt[d])
            else:
                cnt[d] = i
        return ans if odd and even else 0   # 错误
    
class Solution:
    # 暴力
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            odd = even = 0
            a_set = set()
            for j in range(i, n):
                if nums[j] not in a_set:
                    a_set.add(nums[j])
                    if nums[j] % 2:
                        odd += 1
                    else:
                        even += 1
                if odd == even:
                    ans = max(ans, j - i + 1)
        return ans
    

# 2026年2月10日
class Solution:
    # 暴力
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if ans >= n - i + 1:
                break
            odd = even = 0
            a_set = set()
            for j in range(i, n):
                if nums[j] not in a_set:
                    a_set.add(nums[j])
                    if nums[j] % 2:
                        odd += 1
                    else:
                        even += 1
                if odd == even:
                    ans = max(ans, j - i + 1)
        return ans  # 394ms
