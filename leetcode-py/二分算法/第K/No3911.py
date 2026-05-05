# 第 k 小等价于：求最小的 x，满足 ≤x 的数至少有 k 个。
# 第 k 大等价于：求最大的 x，满足 ≥x 的数至少有 k 个。

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        pre_even = [0]
        for i in range(n):
            pre_even.append(pre_even[-1] + (nums[i] % 2 == 0))

        res = []

        for l, r, k in queries:

            def count_missing(i: int):
                return nums[i] // 2 - (pre_even[i + 1] - pre_even[l])

            if count_missing(r) < k:
                base = (nums[r] // 2 * 2)
                res.append(base + (k -count_missing(r)) * 2)
            else:
                lo, hi = l, r + 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if count_missing(mid) >= k:
                        hi = mid
                    else:
                        lo = mid + 1

                if lo == l:
                    res.append(k * 2)
                else:
                    base = (nums[lo - 1] // 2) * 2
                    res.append(base + (k - count_missing(lo - 1)) * 2)

        return res