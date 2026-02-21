from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        ans = n = len(nums)
        for i in range(n):
            if nums[i] % p == target:
                ans = 1
                break
            for j in range(i - 1, -1, -1):
                if i - j + 1 >= ans:
                    break
                nums[j] = (nums[j] + nums[i]) % p
                if nums[j] == target:
                    ans = min(ans, i - j + 1)
        
        return -1 if ans == n else ans  # 超时
    


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        ans = len(nums)
        cnt = defaultdict(int)
        for i, x in enumerate(accumulate(nums)):
            x %= p
            y1 = (x + target) % p
            y2 = (x - target) % p
            if y1 in cnt:
                ans = min(ans, i - cnt[y1])
            if y2 in cnt:
                ans = min(ans, i - cnt[y1])
            cnt[x] = i

        return -1 if ans == len(nums) else ans  # 逻辑存在错误
        

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        ans = len(nums)
        cnt = defaultdict(int)
        cnt[0] = -1
        for i, x in enumerate(accumulate(nums)):
            x %= p
            y = (x - target) % p
            if y in cnt:
                ans = min(ans, i - cnt[y])

            cnt[x] = i

        return -1 if ans == len(nums) else ans  # 91ms


fun = Solution()
fun.minSubarray([4,4,2], 7)