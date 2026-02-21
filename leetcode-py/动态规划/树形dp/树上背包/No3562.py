from bisect import bisect_left
from collections import defaultdict
from functools import cache
from math import inf
from typing import Dict, List


fmax = lambda a, b: b if b > a else a

class Solution:
    # 灵神
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> List[Dict[int, int]]:
            sub_f = [defaultdict(int) for _ in range(2)]
            sub_f[0][0] = sub_f[1][0] = 0
            for y in g[x]:
                fy = dfs(y)
                for k, fyk in enumerate(fy):
                    nf = defaultdict(int)
                    for j, pre_res_y in sub_f[k].items():
                        for jy, res_y in fyk.items():
                            sj = j + jy
                            if sj <= budget:
                                nf[sj] = fmax(nf[sj], pre_res_y + res_y)
                    sub_f[k] = nf

            f = [None] * 2
            for k in range(2):
                res = sub_f[0].copy()
                cost = present[x] // (k + 1)
                if cost <= budget:
                    earn = future[x] - cost
                    for j, res_y in sub_f[1].items():
                        sj = j + cost
                        if sj <= budget:
                            res[sj] = fmax(res[sj], res_y + earn)
                f[k] = res
            return f

        return max(dfs(0)[0].values())  # 615ms
    
class Solution:
    # mipha
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        '''
        树形dp

        1 <= budget <= 160
        '''
        road = defaultdict(list)
        # 单向
        for x,y in hierarchy:
            road[x].append(y)

        m = budget
        # 树形dp
        # 返回 节点 使用了 x 元的最大利润
        # flag 父节点有没有买股票
        @cache
        def dfs(node,flag):
            p,f = present[node-1],future[node-1]
            if flag:
                p //= 2


            # 剪枝
            if p <= m:
                # 子员工 共使用 num 块的最大利润
                # 当前节点买股票
                dp1 = [f-p] * (m + 1)
                # 比 p 小的不存在
                for num in range(p):
                    dp1[num] = -inf
                
                for nxt in road[node]:
                    last = dfs(nxt,True)
                    # 01 背包 不选
                    ndp = dp1.copy()
                    # 01 背包 选
                    for num in range(m+1):
                        # lnum <= m - num
                        for lnum in range(m-num+1):
                            if dp1[num]+last[lnum] > ndp[num+lnum]:
                                ndp[num+lnum]  = dp1[num]+last[lnum]
                            # ndp[num+lnum] = max(ndp[num+lnum],dp1[num]+last[lnum])
                    dp1 = ndp
            else:
                dp1 = [-inf] * (m + 1)

            # 当前节点不买
            dp2 = [0] * (m + 1)
            for nxt in road[node]:
                last = dfs(nxt,False)
                # 01 背包 不选
                ndp = dp2.copy()
                # 01 背包 选
                for num in range(m+1):
                    for lnum in range(m-num+1):
                        if dp2[num]+last[lnum] > ndp[num+lnum]:
                            ndp[num+lnum] = dp2[num]+last[lnum] 
                        # ndp[num+lnum] = max(ndp[num+lnum],dp2[num]+last[lnum])
                dp2 = ndp
                
            # 向后更新
            mx = -inf
            for num in range(m+1):
                if dp1[num] > mx:
                    mx = dp1[num]

                if dp2[num] > mx:
                    mx = dp2[num]
                
                # mx = max(dp1[num],dp2[num],mx)
                dp1[num] = mx
            
            return dp1
                
        res = dfs(1,False)
        dfs.cache_clear()
        return res[-1]  # 10532ms
    

class Solution(object):
    # AI
    def maxProfit(self, n, present, future, hierarchy, budget):
        # 构建树结构，children[i] 存储节点 i 的子节点列表
        children = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            children[u].append(v)
        
        # 记忆化数组，存储每个节点的计算结果
        memo = [None] * (n + 1)
        
        def dfs(u):
            if memo[u] is not None:
                return memo[u]
            
            # 初始化两个 exact 数组，分别对应父节点未选择和选择的情况
            exact0 = [-10**9] * (budget + 1)
            exact1 = [-10**9] * (budget + 1)
            
            # 分别计算父节点状态 s=0 和 s=1 的情况
            for s in [0, 1]:
                # 当前节点 u 的购买价格和利润
                cost_u = present[u-1] if s == 0 else present[u-1] // 2
                profit_u = future[u-1] - cost_u
                
                # f0 表示不选当前节点 u，f1 表示选当前节点 u
                f0 = [-10**9] * (budget + 1)
                f1 = [-10**9] * (budget + 1)
                f0[0] = 0  # 不选 u，花费 0，利润 0
                if cost_u <= budget:
                    f1[cost_u] = profit_u  # 选 u，花费 cost_u，利润 profit_u
                
                # 合并子节点
                for v in children[u]:
                    exact_v0, exact_v1 = dfs(v)  # 获取子节点的 exact 数组
                    # 根据 u 是否被选择，决定使用子节点的哪个 exact 数组
                    # 如果 u 不选，则子节点 v 的父节点状态为 0，使用 exact_v0
                    # 如果 u 选，则子节点 v 的父节点状态为 1，使用 exact_v1
                    new_f0 = [-10**9] * (budget + 1)
                    new_f1 = [-10**9] * (budget + 1)
                    
                    # 合并 f0 和 exact_v0
                    for j in range(budget + 1):
                        if f0[j] >= -10**8:  # 如果 f0[j] 有效
                            for k in range(budget + 1 - j):
                                if exact_v0[k] >= -10**8:
                                    new_f0[j + k] = max(new_f0[j + k], f0[j] + exact_v0[k])
                    # 合并 f1 和 exact_v1
                    for j in range(budget + 1):
                        if f1[j] >= -10**8:
                            for k in range(budget + 1 - j):
                                if exact_v1[k] >= -10**8:
                                    new_f1[j + k] = max(new_f1[j + k], f1[j] + exact_v1[k])
                    
                    f0, f1 = new_f0, new_f1
                
                # 对于当前状态 s，exact 数组为 f0 和 f1 的逐元素最大值
                if s == 0:
                    for j in range(budget + 1):
                        exact0[j] = max(f0[j], f1[j])
                else:
                    for j in range(budget + 1):
                        exact1[j] = max(f0[j], f1[j])
            
            memo[u] = (exact0, exact1)
            return exact0, exact1
        
        # 从根节点 1 开始计算，根节点的父节点视为未选择（s=0）
        exact0, _ = dfs(1)
        
        # 取 exact0 的前缀最大值，即不超过预算的最大利润
        ans = 0
        for j in range(budget + 1):
            ans = max(ans, exact0[j])
        return ans


