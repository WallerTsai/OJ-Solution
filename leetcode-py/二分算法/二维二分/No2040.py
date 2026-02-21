from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    # 二分嵌套
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums2)
        def count(i: int) -> int:
            cnt = 0

            for x in nums1:
                if x > 0:
                    cnt += bisect_right(nums2, i / x)
                elif x < 0:
                    cnt += n - bisect_left(nums2, i / x)
                else:
                    cnt += n if i >= 0 else 0

            return cnt
        
        li = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        MN, MX = min(li), max(li)

        return bisect_left(range(MN, MX + 1), k, key=count) + MN
        # 这里的返回是索引，而我们要的答案通过 索引 + MN 得到
        # 原来的序列为答案序列 [MN, MN + 1, MN + 2 ...... MX]
        # 返回的却是索引       [0, 1, 2 ...... ]

class Solution:
    # 简单版本
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def can(p: int) -> int:
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    cnt += bisect_right(nums2, p / x)
                elif x < 0:
                    cnt += n - bisect_left(nums2, p / x)
                else:
                    cnt += n * int(p >= 0)
            return cnt >= k

        left = -10**11
        right = 10**11

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
class Solution:
    # 灵神
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        i0 = bisect_left(a, 0)  # 四个区域的水平分界线
        j0 = bisect_left(b, 0)  # 四个区域的垂直分界线

        def check(mx: int) -> bool:
            if mx < 0:
                cnt = 0

                # 右上区域
                i, j = 0, j0
                while i < i0 and j < m:  # 不判断 cnt < k 更快
                    if a[i] * b[j] > mx:
                        j += 1
                    else:
                        cnt += m - j
                        i += 1

                # 左下区域
                i, j = i0, 0
                while i < n and j < j0:
                    if a[i] * b[j] > mx:
                        i += 1
                    else:
                        cnt += n - i
                        j += 1
            else:
                # 右上区域和左下区域的所有数都 <= 0 <= mx
                cnt = i0 * (m - j0) + (n - i0) * j0

                # 左上区域
                i, j = 0, j0 - 1
                while i < i0 and j >= 0:
                    if a[i] * b[j] > mx:
                        i += 1
                    else:
                        cnt += i0 - i
                        j -= 1

                # 右下区域
                i, j = i0, m - 1
                while i < n and j >= j0:
                    if a[i] * b[j] > mx:
                        j -= 1
                    else:
                        cnt += j - j0 + 1
                        i += 1

            return cnt >= k

        n, m = len(a), len(b)
        corners = (a[0] * b[0], a[0] * b[-1], a[-1] * b[0], a[-1] * b[-1])
        left, right = min(corners), max(corners)
        return left + bisect_left(range(left, right), True, key=check)