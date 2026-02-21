from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)- 2):
            if nums[i] == 0:
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans if nums[-2] and nums[-1] else -1 # 87ms

class Solution:
    # 差分
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        flip = 0 # 当前位置反转次数
        diff = [0] * (n)
        for i in range(n):
            flip += diff[i]
            if (nums[i] ^ (flip & 1)) == 0:
                if i + 3 > n:
                    return -1
                ans += 1
                flip += 1
                diff[i + 3] -= 1
        return ans  # 105ms

