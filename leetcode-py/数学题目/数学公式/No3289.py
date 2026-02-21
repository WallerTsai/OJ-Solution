from math import isqrt
from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = cnt.most_common(2)
        return [res[0][0], res[1][0]]
    

class Solution:
    # 灵神
    # https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville/solutions/2917852/o1-kong-jian-zuo-fa-pythonjavacgo-by-end-4vpn/
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        a = -n * (n - 1) // 2
        b = -n * (n - 1) * (n * 2 - 1) // 6
        for x in nums:
            a += x
            b += x * x
        x = (a - isqrt(b * 2 - a * a)) // 2
        return [x, a - x]