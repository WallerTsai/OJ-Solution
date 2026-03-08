from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        def func(i: int):
            cnt = defaultdict(int)
            count = 0
            ans = left = 0
            for right, x in enumerate(nums):
                cnt[x] += 1
                if cnt[x] == m:
                    count += 1
                while cnt.__len__() >= i and count >= k:
                    if cnt[nums[left]] == m:
                        count -= 1
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        cnt.pop(nums[left])
                    left += 1
                ans += left
            return ans
        
        return func(k) - func(k + 1)



