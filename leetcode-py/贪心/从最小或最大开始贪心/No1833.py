# 贪心3
# 难度：中等

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        while coins > 0:
            coins -= costs[res]
            res += 1
        if coins != 0:
            res -= 1
        return res
        ### 这种写法存在缺点：1，边界情况处理问题具有不确定性。
        # 2，循环条件建立在硬币买不完雪糕的条件下

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in range(len(costs)):
            coins -= costs[i]
            if coins >= 0:
                res += 1
            else:
                break
        return res  # 94ms
    
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        costs.sort()
        for i in costs:
            if coins >= i:
                res += 1
                coins -= i
            else:
                break
        return res  # 87ms
    
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins >= sum(costs):
            return len(costs)
        res = 0
        costs.sort()
        for i in costs:
            if coins >= i:
                res += 1
                coins -= i
            else:
                break
        return res  # 83ms

class Solution:
    # 该题记录保持代码
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # 找到cost中的最大值来确定count数组的长度
        max_cost = max(costs)
        
        # 创建长度为 max_cost + 1 的计数数组，初始化为0
        count = [0] * (max_cost + 1)
        
        # 统计每个价格的雪糕数量
        for cost in costs:
            count[cost] += 1
        
        # 用于跟踪已花费的金币数和购买的雪糕数
        total_icecreams = 0
        
        # 从价格1到最大价格依次尝试购买雪糕
        for price in range(1, max_cost + 1):
            if count[price] > 0:
                # 如果当前金币数足够购买多支雪糕
                if coins >= price * count[price]:
                    total_icecreams += count[price]
                    coins -= price * count[price]
                else:
                    # 如果金币不够购买所有此价格的雪糕，计算最多能买多少个
                    total_icecreams += coins // price
                    coins = 0  # 将金币用完
                    break  # 金币用完，直接退出循环
        
        return total_icecreams
    
# 时间复杂度
# 第一段代码的时间复杂度是 O(nlogn)，因为需要对 costs 排序；
# 第二段代码的时间复杂度是 O(n+k)，利用计数排序的思想避免了排序操作，其中 k 是 max(costs) 的值。

# 空间复杂度
# 第一段代码的空间复杂度为 𝑂(1)O(1)（若排序为原地操作）或 𝑂(𝑛)O(n)（视排序算法而定）。
# 第二段代码需要额外的计数数组，其空间复杂度为 𝑂(𝑘)O(k)。

# 适用场景
# 第一段代码适合 costs 数据量很大，但价格范围较宽的情况；第二段代码适合 costs 数据量适中，且价格范围较窄的情况。

# 实现复杂度
# 第一段代码简单直观，直接对 costs 排序后进行贪心选择；第二段代码稍复杂，需统计价格分布并逐步计算购买能力。

# 潜在问题
# 第一段代码的排序操作可能在数据量非常大时带来性能瓶颈；第二段代码在价格范围过大（如百万级别）时，会浪费大量空间用于计数数组。