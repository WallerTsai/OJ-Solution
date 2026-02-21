from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res = left = 0
        for right,num in enumerate(nums):
            cnt[num] += 1
            while sum(cnt.values()) - max(cnt.values()) > k:
                cnt[nums[left]] -= 1
                left += 1
            index = left
            remove_n = k
            while nums[index] != num:
                index += 1
                remove_n -= 1
            res = max(res,right-index+1 - remove_n)
        return res  # 错误且超时

class Solution:
    # 灵神
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans

class Solution:
    # 灵神 + 小优化
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                if p - pos[left] > k:  # 要删除的数太多了
                    left += 1
            ans = max(ans, right - left + 1)
        return ans  # 291ms