from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = defaultdict(list)
        for u, v, cost in edges:
            g[u].append((v, cost))
        
        ans = -1

        def dfs(i: int, cur: int, sum: int):
            nonlocal ans
            if sum > k:
                return
            if cur <= ans:
                return
            
            if i == n - 1:
                ans = max(ans, cur)

            for v, cost in g[i]:
                if not online[v]:
                    continue
                nx_cur = min(cur, cost)
                nx_sum = sum + cost
                dfs(v, nx_cur, nx_sum)

        dfs(0, inf, 0)

        return ans
    

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = defaultdict(list)
        for u, v, cost in edges:
            g[u].append((v, cost))
        
        ans = -1

        def dfs(i: int, cur_min: int, total: int):
            nonlocal ans
            if total > k:
                return
            if cur_min <= ans:
                return
            
            if i == n - 1:
                ans = max(ans, cur_min)

            for v, cost in g[i]:
                if not online[v]:
                    continue
                nx_cur = min(cur_min, cost)
                nx_sum = total + cost
                dfs(v, nx_cur, nx_sum)

        dfs(0, inf, 0)

        return ans
    
# 以上弱数据更快通过

class Solution:
    # 二分 + DAG DP
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # 建图
        g = defaultdict(list)
        right = -1
        for u, v, cost in edges:
            if online[u] and online[v]:
                g[u].append((v, cost))
                if u == 0:
                    right = max(right, cost)

        def check(lower: int) -> bool:
            @cache
            def dfs(x: int) -> int:
                if x == n - 1:
                    return 0
                res = inf
                for v, cost in g[x]:
                    if cost >= lower:
                        res = min(res, dfs(v) + cost)
                return res
            return dfs(0) <= k
        
        left = 0
        right += 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1 # 2689ms


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        '''
        最短路 + 二分答案
        '''
        # 建图
        road = defaultdict(list)
        for x,y,c in edges:
            # 移除离线点
            if not online[x] or not online[y]:
                continue
            road[x].append((y,c))
            
        n = len(online)
        def check(limit):
            tgt = n - 1
            heap = [(0,0)]
            # 到达这个点的最小总成本
            dist = {}
            dist[0] = 0
            while heap:
                t,node = heappop(heap)
                if dist[node] < t:
                    continue

                if node == tgt:
                    return True

                for nxt,c in road[node]:
                    nt = t + c
                    # 低于限制 或者 超出成本限制
                    if c < limit or nt > k:
                        continue
                    if nxt not in dist or dist[nxt] > nt:
                        dist[nxt] = nt
                        heappush(heap,(nt,nxt))

            return False

            
        # 二分答案
        start = 0
        end = int(1e9)
        while start <= end:
            middle = (start + end) // 2
            if check(middle):
                start = middle + 1
            else:
                end = middle - 1
                
        return start - 1


fun = Solution()
fun.findMaxPathScore([[0,1,5],[1,3,10],[0,2,3],[2,3,4]], [True,True,True,True], 10)