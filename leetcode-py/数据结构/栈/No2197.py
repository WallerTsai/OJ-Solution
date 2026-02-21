from math import gcd, lcm
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        li = [nums[0]]
        n = len(nums)
        if n == 1:
            return li
        for i in range(1, n):
            if gcd(li[-1], nums[i]) > 1:
                li[-1] = lcm(li[-1], nums[i])
            else:
                li.append(nums[i])
        return li   # 错误

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = [nums[0]]
        n = len(nums)
        if n == 1:
            return st
        for i in range(1, n):
            temp = nums[i]
            while st and gcd(st[-1], temp) > 1:
                temp = lcm(st.pop(), temp)
            st.append(temp)
        return st

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            while st and gcd(x, st[-1]) > 1:
                x = lcm(x, st.pop())
            st.append(x)
        return st