from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        n = max(nums).bit_length()
        for i in range(n - 1, -1, -1):
            mask |= 1 << i
            # 两数之和
            target = ans | (1 << i)
            _set = set()
            for x in nums:
                x &= mask   # 低于 i 的比特位置为 0
                if x ^ target in _set:
                    ans = target
                    break
                _set.add(x)
        return ans


