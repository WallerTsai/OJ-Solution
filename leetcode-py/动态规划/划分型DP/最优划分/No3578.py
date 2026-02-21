from collections import deque
from functools import cache
import heapq
from math import inf
from typing import List

fmax = lambda x, y : x if x > y else y
fmin = lambda x, y : x if x < y else y
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 **9  + 7
        n = len(nums)

        @cache
        def dfs(i: int):
            res = 0

            if i >= n:
                return 1 
            
            # 分割
            res = (res + dfs(i + 1)) % MOD

            # 不分割
            mn = mx = nums[i]
            for j in range(i + 1, len(nums)):
                mx = fmax(mx, nums[j])
                mn = fmin(mn, nums[j])
                if mx - mn > k:
                    break
                res = (res + dfs(j + 1)) % MOD

            return res

        return dfs(0)   # 超时 卡在例869


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 **9  + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[n] = 1
        suf_sum = [0] * (n + 1)
        suf_sum[n] = 1
        for i in range(n - 1, -1, -1):
            dp[i]  = (dp[i]  + dp[i + 1]) % MOD

            mn = mx = nums[i]
            for j in range(i + 1, n):
                mx = fmax(mx, nums[j])
                mn = fmin(mn, nums[j])
                if mx - mn > k:
                    break
                dp[i]  = (dp[i]  + dp[j + 1]) % MOD

        return dp[0]    # 超时 卡在869
    
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 **9  + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[n] = 1
        suf_sum = [0] * (n + 2)
        suf_sum[n] = 1
        max_heap = []
        min_heap = []
        ptr_right = n - 1
        for i in range(n - 1, -1, -1):
            dp[i]  = (dp[i]  + dp[i + 1]) % MOD

            heapq.heappush(max_heap, (-nums[i], i))
            heapq.heappush(min_heap, (nums[i], i))
            while True:
                # 清理窗口
                while max_heap and max_heap[0][1] > ptr_right:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] > ptr_right:
                    heapq.heappop(min_heap)
                
                cur_max, cur_min = -max_heap[0][0], min_heap[0][0]

                if cur_max - cur_min <= k:
                    break

                ptr_right -= 1
            dp[i] = (dp[i] + suf_sum[i + 1] - suf_sum[ptr_right + 1]) % MOD
            suf_sum[i] = (suf_sum[i + 1] + dp[i]) % MOD

        return dp[0]    # 错误

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 **9  + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[n] = 1
        suf_sum = [0] * (n + 2)
        suf_sum[n] = 1
        max_heap = []
        min_heap = []
        ptr_right = n - 1
        for i in range(n - 1, -1, -1):

            heapq.heappush(max_heap, (-nums[i], i))
            heapq.heappush(min_heap, (nums[i], i))
            while True:
                # 清理窗口
                while max_heap and max_heap[0][1] > ptr_right:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] > ptr_right:
                    heapq.heappop(min_heap)
                
                cur_max, cur_min = -max_heap[0][0], min_heap[0][0]

                if cur_max - cur_min <= k:
                    break

                ptr_right -= 1

            # 计算 dp[i]
            dp[i] = (suf_sum[i + 1] - suf_sum[ptr_right + 2]) % MOD
            
            # 更新后缀和
            suf_sum[i] = (dp[i] + suf_sum[i + 1]) % MOD

        return dp[0]    # 1039ms    Nlogn
    
class Solution:
    # 灵神
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        min_q = deque()
        max_q = deque()
        f = [0] * (n + 1)
        f[0] = 1
        sum_f = 0  # 窗口中的 f[i] 之和
        left = 0

        for i, x in enumerate(nums):
            # 1. 入
            sum_f += f[i]

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            # 2. 出
            while nums[max_q[0]] - nums[min_q[0]] > k:
                sum_f -= f[left]
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 3. 更新答案
            f[i + 1] = sum_f % MOD

        return f[n] # 347ms N

fun = Solution()
fun.countPartitions([9,4,1,3,7], 4) # [6, 6, 3, 2, 1, 1]