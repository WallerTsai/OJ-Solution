from functools import cache
from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        right = 1
        while right < n:
            start = right
            right += 1
            if right == n:
                break
            d = nums[right] - nums[right - 1]
            while right < n and nums[right] - nums[right - 1] == d:
                right += 1
            ans = max(ans, right - start + 1)
        return ans  # 错误
        

class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        left = 0
        right = 1
        while left < n:
            right = left + 1
            if right == n:
                break

            d = nums[right] - nums[left]
            k = 1
            nxt_left = right
            pre = nums[left]
            
            while right < n:
                if nums[right] - pre != d and k:
                    nxt_left = right - 1
                    k -= 1
                    pre = pre + d
                elif nums[right] - pre == d:
                    pre = nums[right]
                else:
                    break
                right += 1
            ans = max(ans, right - left + k)
            left = nxt_left
        return ans  # 错误
            
# 以下代码参考灵神
class Solution:
    # 前后缀分解
    def calc(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        pre[0] = 1
        pre[1] = 2
        for i in range(2, n):
            if nums[i - 2] + nums[i] == nums[i - 1] * 2:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = 2
        return pre
    
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        pre = self.calc(nums)
        ans = max(pre) + 1
        if ans >= n:
            return n
        
        suf = self.calc(nums[::-1])[::-1]
        
        for i in range(1, n - 1):
            # 把 nums[i] 改成 d2/2
            d2 = nums[i + 1] - nums[i - 1]
            if d2 % 2:
                continue
            d = d2 // 2

            ok_left = i > 1 and nums[i - 1] - nums[i - 2] == d
            ok_right = i + 2 < n and nums[i + 2] - nums[i + 1] == d

            if ok_left and ok_right:
                ans = max(ans, pre[i - 1] + 1 + suf[i + 1])
            elif ok_left:
                ans = max(ans, pre[i - 1] + 2)
            elif ok_right:
                ans = max(ans, 2 + suf[i + 1])
        
        return ans


class Solution:
    # 灵神
    # 分组循环
    def longestArithmetic(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 1
        while True:
            # 枚举 i-1 和 i 作为等差子数组的前两项，且我们不改 nums[i-1] 和 nums[i]
            start = i - 1
            d = nums[i] - nums[i - 1]

            # 往右移动，直到 nums[i] 不满足等差
            i += 1
            while i < n and nums[i] - nums[i - 1] == d:
                i += 1

            # 现在 [start, i-1] 是等差子数组
            # 要想让子数组更长，要么改 nums[start-1]，要么改 nums[i]

            # 改 nums[start-1]
            if start >= 2 and nums[start] - nums[start - 2] == d * 2:  # 可以和 nums[start-2] 连起来
                ans = max(ans, i - start + 2)  # 等差子数组 [start-2, i-1]
                # 继续往左延长的情况等同于上一段继续往右延长，无需重复计算
            else:  # 子数组左端点最远只能到 max(start-1,0)
                ans = max(ans, i - max(start - 1, 0))  # 等差子数组 [max(start-1,0), i-1]

            if i == n:
                return ans

            # 改 nums[i]
            if i < n - 1 and nums[i + 1] - nums[i - 1] == d * 2:  # 可以和 nums[i+1] 连起来
                # 继续往右延长
                j = i + 2
                while j < n and nums[j] - nums[j - 1] == d:
                    j += 1
                ans = max(ans, j - start)  # 等差子数组 [start, j-1]
            else:  # 子数组右端点最远只能到 i
                ans = max(ans, i - start + 1)  # 等差子数组 [start, i]

# 状态机DP
class Solution:
    # 灵神
    def longestArithmetic(self, nums: List[int]) -> int:
        # 返回以 i 结尾的最长等差子数组的长度，其中 nums[i] 不改
        # left 表示剩余操作次数
        @cache
        def dfs(i: int, left: int) -> int:
            if i <= 1:
                return i + 1  # 等差子数组 [0, i]，长为 i+1

            # 不改
            res = 2  # 等差子数组 [i-1, i]，长为 2
            if nums[i - 2] + nums[i] == nums[i - 1] * 2:  # 三个数等差
                res = dfs(i - 1, left) + 1  # 以 i-1 结尾的最长等差子数组 + [i, i]

            if left:
                res = max(res, 3)  # 改 nums[i-2]，得到等差子数组 [i-2, i]，长为 3
                if i >= 3:
                    # 改 nums[i-1]
                    if (nums[i - 2] - nums[i - 3]) * 2 == nums[i] - nums[i - 2]:
                        res = max(res, dfs(i - 2, 0) + 2)  # 以 i-2 结尾的最长等差子数组 + [i-1, i]

                    # 改 nums[i-2]
                    d = nums[i] - nums[i - 1]
                    if nums[i - 1] - nums[i - 3] == d * 2:
                        res = max(res, 4)  # 等差子数组 [i-3, i]，长为 4
                        if i >= 4 and nums[i - 3] - nums[i - 4] == d:
                            res = max(res, dfs(i - 3, 0) + 3)  # 以 i-3 结尾的最长等差子数组 + [i-2, i]

            return res

        n = len(nums)
        ans1 = max(dfs(i, 1) for i in range(n))  # 不改 nums[i]
        ans2 = max(dfs(i - 1, 0) for i in range(1, n)) + 1  # 改 nums[i]
        return max(ans1, ans2)

# 手写 max 更快
fmax = lambda a, b: b if b > a else a

class Solution:
    # 灵神
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n)]
        f[0][0] = f[0][1] = 1
        f[1][0] = f[1][1] = 2
        for i in range(2, n):
            for left in range(2):
                # 不改
                res = 2  # 等差子数组 [i-1, i]，长为 2
                if nums[i - 2] + nums[i] == nums[i - 1] * 2:  # 三个数等差
                    res = f[i - 1][left] + 1  # 以 i-1 结尾的最长等差子数组 + [i, i]

                if left:
                    res = fmax(res, 3)  # 改 nums[i-2]，得到等差子数组 [i-2, i]，长为 3
                    if i >= 3:
                        # 改 nums[i-1]
                        if (nums[i - 2] - nums[i - 3]) * 2 == nums[i] - nums[i - 2]:
                            res = fmax(res, f[i - 2][0] + 2)  # 以 i-2 结尾的最长等差子数组 + [i-1, i]

                        # 改 nums[i-2]
                        d = nums[i] - nums[i - 1]
                        if nums[i - 1] - nums[i - 3] == d * 2:
                            res = fmax(res, 4)  # 等差子数组 [i-3, i]，长为 4
                            if i >= 4 and nums[i - 3] - nums[i - 4] == d:
                                res = fmax(res, f[i - 3][0] + 3)  # 以 i-3 结尾的最长等差子数组 + [i-2, i]

                f[i][left] = res

        ans1 = max(f[i][1] for i in range(n))  # 不改 nums[i]
        ans2 = max(f[i][0] for i in range(n - 1)) + 1  # 改 nums[i+1]
        return max(ans1, ans2)

print(Solution().longestArithmetic([9,7,5,10,1]))
print(Solution().longestArithmetic([1,2,6,7]))