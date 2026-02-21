from itertools import pairwise
from math import inf
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        ans = 0
        while i < n:
            pre = nums[i]
            flag = 0
            cur_length = 1
            next_start = i + 1
            for j in range(i + 1, n):
                if nums[j] >= pre:
                    cur_length += 1
                    pre = nums[j]
                elif flag == 0:
                    cur_length += 1
                    flag = 1
                    next_start = j
                else:
                    break
            ans = max(cur_length, ans)
            i = next_start
        return ans  # 错误 [3,-4,-2] 输出 2 预期 3


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        ans = 0
        while i < n:
            pre = nums[i]
            flag = 0
            cur_length = 1
            next_start = i + 1
            for j in range(i + 1, n + 1):
                if j == n:
                    return max(ans, cur_length)
                if nums[j] >= pre:
                    cur_length += 1
                    pre = nums[j]
                elif flag == 0:
                    if cur_length < 3:
                        pre = min(pre, nums[j])
                    cur_length += 1
                    flag = 1
                    next_start = max(next_start, j - 1)
                else:
                    break
            ans = max(cur_length, ans)
            i = next_start
        return ans      # 错误
    

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        ans = 0
        while i < n:
            pre = i
            flag = 0
            cur_length = 1
            next_start = i + 1
            for j in range(i + 1, n + 1):
                if j == n:
                    return max(ans, cur_length)
                if nums[j] >= nums[pre]:
                    cur_length += 1
                    pre += 1
                elif flag == 0:
                    if cur_length < 3:
                        pre = min(pre, nums[j])
                    cur_length += 1
                    flag = 1
                    next_start = max(next_start, j - 1)
                else:
                    break
            ans = max(cur_length, ans)
            i = next_start
        return ans  # 错误
            

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        last_drop = -1
        max_len = 1
        
        for right in range(1, n):
            if nums[right] < nums[right - 1]:
                if last_drop != -1:
                    left = last_drop + 1
                last_drop = right - 1
            max_len = max(max_len, right - left + 1)
        
        return max_len  # 错误




# 枚举要替换的位置 i。如果 a[i-1] ≤ a[i+1]，则我们可以把 a[i] 改成一个 [a[i-1], a[i+1]] 之间的数，将前后连起来；否则，a[i] 只能作为子数组的开头或结尾，无法连接前后。
# 连起来以后，这个不降子数组的长度就是以 (i-1) 为结尾的不降子数组长度，加上以 (i+1) 为开头的不降子数组长度，再加一。通过递推可以求出以每个下标为开头（结尾）的不降子数组长度。
# 复杂度 O(n)。

class Solution:
    # 妙蛙种子
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # 添加哨兵元素 -INF 和 +INF，这样就不用处理下标越界的情况
        nums = [-inf] + nums + [inf]

        # f[i]：以下标 i 为结尾的不降子数组长度
        f = [0] * (n + 2)
        f[0] = 0
        for i in range(1, n + 1):
            if nums[i] >= nums[i - 1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = 1
        
        # g[i]：以下标 i 为开头的不降子数组长度
        g = [0] * (n + 2)
        g[n + 1] = 0
        for i in range(n, 0, -1):
            if nums[i] <= nums[i + 1]:
                g[i] = g[i + 1] + 1
            else:
                g[i] = 1

        ans = 0
        for i in range(1, n + 1):
            # 前后可以连接
            if nums[i - 1] <= nums[i + 1]:
                ans = max(ans, f[i - 1] + g[i + 1] + 1)
            else:
                ans = max(ans, f[i - 1] + 1, g[i + 1] + 1)
        return ans

fun = Solution()
fun.longestSubarray([1,2,3,1,2])
