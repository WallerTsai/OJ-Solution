from math import lcm
from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        if r2 < r1:
            d2, d1 = d1, d2
            r2, r1, = r1, r2

        t = 1
        while d1 or d2:
            if d1 and t % r1:
                d1 -= 1
            elif d2 and t % r2:
                d2 -= 1
            t += 1

        return t - 1    # 错误
    
# 由于数据范围过大，可以考虑二分
class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        r3 = lcm(r1, r2)

        def check(t: int):
            t1 = t - t // r1
            t2 = t - t // r2
            t3 = t // r3
            return t1 >= d1 and t2 >= d2 and t - t3 >= d1 + d2
        
        left, right = 1, (d1 + d2) * max(r1, r2) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
    

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        r3 = lcm(r1, r2)

        def check(t: int):
            t1 = t - t // r1
            t2 = t - t // r2
            t3 = t // r3
            return t1 >= d1 and t2 >= d2 and t - t3 >= d1 + d2
        
        left, right = 1, (d1 + d2) * 2 + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


# 二分以及数学公式推导证明：
# https://leetcode.cn/problems/minimum-time-to-complete-all-deliveries/solutions/3821373/liang-chong-fang-fa-er-fen-da-an-shu-xue-vyqv/

class Solution:
    # 灵神
    # 数学推导 + 公式
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        l = lcm(r1, r2)

        def f(d: int, r: int) -> int:
            return d + (d - 1) // (r - 1)

        return max(f(d1, r1), f(d2, r2), f(d1 + d2, l))


fun = Solution()
fun.minimumTime([1, 3], [2, 2])