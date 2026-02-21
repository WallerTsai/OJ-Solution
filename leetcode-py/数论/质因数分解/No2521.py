from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            i = 2
            while i ** 2 <= x:  # 枚举
                if x % i == 0:
                    s.add(i)
                    x //= i
                    while x % i == 0:   # 还是含有 i 因子
                        x //= i
                i += 1
            if x > 1:   # 余下的质因子
                s.add(x)
        return len(s)