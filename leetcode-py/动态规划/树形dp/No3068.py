from math import inf
from typing import List

# 难在 定义状态 和 找到转移方程

# u,v 分别为父，子 节点
# 如果 u 最后通过 v 转移过来的状态是 不异或
#     · 如果 v 选择 不异或 那么 dp[u][0] = dp[v][0] + nums[u]
#     · 如果 v 选择了 异或 那么 dp[u][0] = dp[v][1] + nums[u] ^ k
# 如果 u 最后通过 v 转移过来的状态是 异或
#     · 如果 v 选择 不异或 那么 dp[u][1] = dp[v][1] + nums[u]
#     · 如果 v 选择了 异或 那么 dp[u][1] = dp[v][0] + nums[u] ^ k

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # 建图
        g = [[] for _ in nums]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(u: int, fa: int):
            u0, u1 = 0, -inf
            for v in g[u]:
                if v != fa:
                   v0, v1 = dfs(v,u)
                   u0, u1 = max(u0 + v0, u1 + v1), max(u1 + v0, u0 + v1)    # 两种情况，一种是只有一个子节点，一种有两个子节点
            return max(u0 + nums[u], u1 + (nums[u] ^ k)), max(u1 + nums[u], u0 + (nums[u] ^ k))

        return dfs(0,-1)[0]
    
class Solution:
    # 羊神
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dp0, dp1 = 0, -inf
        for num in nums:
            dp0, dp1 = max(dp0 + num, dp1 + (num ^ k)), max(dp0 + (num ^ k), dp1 + num)
        return dp0