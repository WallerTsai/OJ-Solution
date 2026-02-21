from bisect import bisect_left
from functools import cache
from math import inf
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, flag: int) -> int:
            # flag: -1 高出低进 0 未持有 1 低进高出 
            if j < 0:
                return -inf
            if i < 0:
                return -inf if flag else 0
            if flag == 1:
                return max(dfs(i - 1, j, flag), dfs(i - 1, j, 0) - prices[i])
            elif flag == -1:
                return max(dfs(i - 1, j, flag), dfs(i - 1, j, 0) + prices[i])
            return max(dfs(i - 1, j, 0), dfs(i - 1, j - 1, 1) + prices[i], dfs(i - 1, j - 1, -1) - prices[i])

        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans  # 5540ms


class Solution:
    # 递推
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[-inf] * 3 for _ in range(k + 2)] for _ in range(n + 1)]
        # dp[][][0] 未持有 | dp[][][1] 低进高出 | dp[][][2] 高出低进
        for j in range(1, k + 2):
            dp[0][j][0] = 0
        
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + p, dp[i][j - 1][-1] - p)
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - p)
                dp[i + 1][j][-1] = max(dp[i][j][-1], dp[i][j][0] + p)
        
        return dp[n][-1][0] # 3218ms


class Solution:
    # 递推
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[-inf] * 3 for _ in range(k + 2)]
        # dp[][0] 未持有 | dp[][1] 低进高出 | dp[][2] 高出低进
        for j in range(1, k + 2):
            dp[j][0] = 0
        
        for p in prices:
            for j in range(1, k + 2):
                dp[j][1] = max(dp[j][1], dp[j][0] - p)
                dp[j][-1] = max(dp[j][-1], dp[j][0] + p)
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + p, dp[j - 1][-1] - p)
        
        return dp[-1][0] ### 虽然能过，但是是错误的
        # 当处理到 j 时，j-1 已经在本轮循环中处理过了
        # 所以 dp[j-1][1] 和 dp[j-1][-1] 已经是今天更新后的值
        # 但我们需要的是前一天的值

class Solution:
    # 递推
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[-inf] * 3 for _ in range(k + 2)]
        # dp[][0] 未持有 | dp[][1] 低进高出 | dp[][2] 高出低进
        for j in range(1, k + 2):
            dp[j][0] = 0
        
        for p in prices:
            for j in range(k + 1, 0, -1):
                dp[j][1] = max(dp[j][1], dp[j][0] - p)
                dp[j][-1] = max(dp[j][-1], dp[j][0] + p)
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + p, dp[j - 1][-1] - p)
        
        return dp[-1][0]
    


# 2025年12月17日
from functools import cache
from math import inf
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, flag):
            if j < 0:
                return -inf
            
            if i < 0:
                return -inf if flag else 0
            
            if flag == 1:
                return max(dfs(i - 1, j, flag), dfs(i - 1, j - 1, 0) - prices[i])
            elif flag == -1:
                return max(dfs(i - 1, j, flag), dfs(i - 1, j - 1, 0) + prices[i])
            else:
                return max(dfs(i - 1, j, flag), dfs(i - 1, j, 1) + prices[i], dfs(i - 1, j, -1) - prices[i])
            
        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans
    
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[[-inf, -inf, -inf] for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0

        for i in range(n):
            for j in range(k + 2):
                dp[i + 1][j + 1][0] = max(dp[i][j + 1][0], dp[i][j][1] + prices[i], dp[i][j][-1] - prices[i])
                dp[i + 1][j + 1][1] = max(dp[i][j + 1][1], dp[i][j + 1][0] - prices[i])
                dp[i + 1][j + 1][-1] = max(dp[i][j + 1][-1], dp[i][j + 1][0] + prices[i])

        return dp[n][k + 1][0]    
    

class Solution:
    # leetcode最快
    def maximumProfit(self, prices: List[int], k: int) -> int:
        def cal(x):
            f, g, h = (0, 0), (-inf, 0), (-inf, 0)
            for p in prices:
                f0, g0, h0 = f, g, h
                f = max(f0, (g0[0] + p - x, g0[1] - 1), (h0[0] - p - x, h0[1] - 1))
                g = max(g0, (f0[0] - p, f0[1]))
                h = max(h0, (f0[0] + p, f0[1]))
            return f[0], -f[1]

        def check(x):
            return cal(x)[1] <= k
        cost = bisect_left(range(max(prices)), True, key=check)
        s, c = cal(cost)
        return s + k * cost

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # --- 核心辅助函数：计算在指定手续费下的最优利润 ---
        # x: 我们人为引入的“每笔交易手续费”（惩罚值）
        # 这个费用的作用是：费用越高，为了保证利润，算法就会自愿减少交易次数。
        def cal(x):
            # 初始化状态：(当前利润, -当前交易次数)
            # 使用 -交易次数 是因为 Python 的 max 函数比较元组时：
            # 1. 先比较第一个元素（利润），利润越大越好。
            # 2. 如果利润相同，比较第二个元素。我们希望交易次数越少越好（避免不必要的交易），
            #    即“交易次数”越小越好，也就是“-交易次数”越大越好。
            #    例如：-3 > -5，max 会选择 -3（代表 3 次交易），而不是 -5（代表 5 次交易）。
            
            f = (0, 0)      # f: 空仓状态（当前不持有股票，也不欠股票）
            g = (-inf, 0)   # g: 多头状态（当前持有股票，等待卖出）
            h = (-inf, 0)   # h: 空头状态（当前做空股票，等待买回）
            
            for p in prices:
                f0, g0, h0 = f, g, h # 保存上一天的状态，避免脏读
                
                # --- 更新 f (空仓) ---
                # 我们可以从三种情况转移到 f：
                # 1. f0: 昨天也是空仓，今天不动。
                # 2. g0: 昨天持有股票(多头)，今天卖出平仓。利润增加 p，扣除手续费 x，交易次数+1。
                # 3. h0: 昨天做空股票(空头)，今天买回平仓。利润减少 p (因为是买入)，扣除手续费 x，交易次数+1。
                # 注意：这里选择在“平仓”时结算手续费 x 和增加计数。
                f = max(f0, 
                        (g0[0] + p - x, g0[1] - 1), 
                        (h0[0] - p - x, h0[1] - 1))
                
                # --- 更新 g (多头/持有) ---
                # 1. g0: 昨天就持有，今天不动。
                # 2. f0: 昨天空仓，今天买入开多单。利润减少 p。
                g = max(g0, 
                        (f0[0] - p, f0[1]))
                
                # --- 更新 h (空头/做空) ---
                # 1. h0: 昨天就做空，今天不动。
                # 2. f0: 昨天空仓，今天卖出开空单。利润增加 p。
                h = max(h0, 
                        (f0[0] + p, f0[1]))
            
            # 返回最终结果：(最大利润, 正数的实际交易次数)
            return f[0], -f[1]

        # --- 二分查找检查函数 ---
        # 检查当手续费为 x 时，最优策略的交易次数是否 <= k
        def check(x):
            return cal(x)[1] <= k

        # --- WQS 二分主逻辑 ---
        # 我们在 range(max(prices)) 范围内二分查找手续费 cost。
        # 逻辑：
        # - 手续费 x 越小，交易越频繁，次数 > k (check 返回 False)
        # - 手续费 x 越大，交易越少，次数 <= k (check 返回 True)
        # 我们要找的是第一个让次数 <= k 的最小手续费（bisect_left 的功能）。
        # 上界 max(prices) 是因为如果手续费超过股价，根本不可能盈利，交易次数必为 0。
        cost = bisect_left(range(max(prices) + 1), True, key=check)
        
        # 使用找到的最佳手续费 cost 再次计算
        s, c = cal(cost)
        
        # --- 还原真实利润 ---
        # s 是扣除了 (实际交易次数 * cost) 后的利润。
        # 题目要求的是总利润，不包含这个虚拟手续费，所以要加回来。
        # 注意：这里加的是 k * cost 而不是 c * cost。
        # 原因：当 cost 恰好让多个点共线时，c 可能小于 k，但数学上可以通过线性插值视为 k 次。
        # 加上 k * cost 可以消除二分带来的误差，得到恰好 k 次（或限制下最优）的真实利润。
        return s + k * cost # 538ms
    

class Solution:
    # yiren
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # 自定义比较函数：优先利润高，利润相同优先交易次数少
        def max2(a, b):
            return a if (a[0] > b[0] or (a[0] == b[0] and a[1] < b[1])) else b

        def dp(p):
            f0, f1, f2 = [0, 0], [-float('inf'), 0], [-float('inf'), 0]
            for x in prices:
                nf0 = f0.copy()
                # 状态转移：f0(空仓), f1(多头), f2(空头)
                nf0 = max2(max2(nf0, [f1[0] + x - p, f1[1] + 1]), [f2[0] - x - p, f2[1] + 1])
                f1 = max2(f1, [f0[0] - x, f0[1]])
                f2 = max2(f2, [f0[0] + x, f0[1]])
                f0 = nf0
            return f0

        # 1. 预先检查：如果 k 足够大（相当于 cost=0），直接返回
        f = dp(0)
        if f[1] <= k:
            return f[0]

        # 2. WQS 二分：左闭右开写法 [l, r)
        left = 0
        right = max(prices) + 1  # 右边界设为足够大，确保覆盖 [0, max(prices)+1]
        
        # 不需要 ans 变量暂存，l 最终会收敛到目标 cost
        while left < right:
            mid = (left + right) // 2
            f = dp(mid)
            
            if f[1] <= k:
                # 交易次数 <= k，满足条件。
                # 我们希望找到满足条件的“最小” cost（或者最接近边界的），
                # 同时因为是左闭右开，r = mid 表示保留 mid 作为潜在解，并向左收缩。
                right = mid
            else:
                # 交易次数 > k，不满足条件。
                # 说明 cost 太低了，需要增加 cost 来减少交易次数。
                # mid 肯定不可行，l = mid + 1。
                left = mid + 1
        
        # 3. 此时 l 就是满足 f[1] <= k 的最小 cost
        # 根据 WQS 二分原理，直接利用公式计算结果
        f = dp(left)
        return k * left + f[0]  # 296ms