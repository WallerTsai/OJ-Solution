from functools import cache
import heapq
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k > n // 2:
            return -1
        @cache
        def dfs(i: int, k: int, pre: bool, f: bool):
            if i == n:
                if k <= 0:
                    return 0
                return inf
            
            if i == n - 1 and not f:
                return dfs(i + 1, k, False, f)

            res = 0
            if not pre:
                t = 0
                if nums[i] <= nums[(i - 1) % n] or nums[i] <= nums[(i + 1) % n]:
                    t = max(nums[(i - 1) % n], nums[(i + 1) % n]) - nums[i] + 1
                nx_f = f
                if i == 0:
                    nx_f = False
                res = min(res, t + dfs(i + 1, k - 1, True, nx_f))

            res = min(res, dfs(i + 1, k, False, f))
            return res

        ans = dfs(0, k, False, True)
        dfs.cache_clear()
        return ans  # 错误
    


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k > n // 2:
            return -1
        
        cost  = [0] * n
        for i in range(n):
            neig = max(nums[(i - 1) % n], nums[(i + 1) % n])
            cost[i] = max(neig - nums[i] + 1, 0)

        # 打家劫舍
        def rob(li: List[int], t: int):
            m = len(li)
            if t == 0:
                return 0
            
            a = [0] + [inf] * k
            b = [0] + [inf] * k

            for i in range(m):
                c = li[i]
                new_dp = b[:]
                for j in range(1, (min(t, i // 2 + 1)) + 1):
                    val = a[j - 1] + c
                    if val < new_dp[j]:
                        new_dp[j] = val
                
                a = b
                b = new_dp

            return b[t]
        
        ans = min(rob(cost[1:], k), cost[0] + rob(cost[2: -1], k - 1))

        return ans if ans != inf else -1

# 反悔贪心
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1

        cnt = 0
        for i in range(n):
            if nums[i - 1] < nums[i] > nums[(i + 1) % n]:
                cnt += 1
        if cnt >= k:
            return 0
        
        cost = [0] * n
        for i in range(n):
            left = nums[i - 1]
            right = nums[(i + 1) % n]
            cost[i] = max(0, max(left, right) - nums[i] + 1)

        # 初始化双向链表 (用数组模拟，L存储左邻居下标，R存储右邻居下标)
        L = [(i - 1) % n for i in range(n)]
        R = [(i + 1) % n for i in range(n)]

        heap = [(cost[i], i) for i in range(n)]
        heapq.heapify(heap)
        deleted = [False] * n
        ans = 0
        for _ in range(k):
            while heap and deleted[heap[0][1]]:
                heapq.heappop(heap)

            c, i = heapq.heappop(heap)
            ans += c

            l, r = L[i], R[i]
            deleted[l] = True
            deleted[r] = True

            # 更新当前位置为“反悔节点”
            cost[i] = cost[l] + cost[r] - cost[i]
            heapq.heappush(heap, (cost[i], i))

            # 更新指针
            L[i] = L[l]
            R[i] = R[r]

            R[L[i]] = i
            L[R[i]] = i

        return ans