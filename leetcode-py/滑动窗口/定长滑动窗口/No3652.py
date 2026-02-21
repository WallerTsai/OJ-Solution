from itertools import accumulate
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ans = total = sum(prices[i] * strategy[i] for i in range(len(prices)))

        diff_max = 0
        for i in range(k):
            if i < k // 2:
                diff_max -= prices[i] * strategy[i]
            else:
                diff_max += prices[i] * (1 - strategy[i])

        if total + diff_max > ans:
            ans = total + diff_max


        for i in range(k, len(prices)):
            diff_max += prices[i] * (1 - strategy[i])
            diff_max -= prices[i - k // 2]
            diff_max += prices[i - k] * strategy[i - k]
            if total + diff_max > ans:
                ans = total + diff_max

        return ans  # 183ms
    
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        total = max_s = s = 0
        for i, (p, st) in enumerate(zip(prices, strategy)):
            total += p * st
            # 1. 入
            s += p * (1 - st)
            if i < k - 1:  # 窗口长度不足 k
                if i >= k // 2 - 1:
                    s -= prices[i - k // 2 + 1]
                continue
            # 2. 更新
            max_s = max(max_s, s)
            # 3. 出
            s -= prices[i - k // 2 + 1] - prices[i - k + 1] * strategy[i - k + 1]
        return total + max_s


# 2025年12月18日
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # 双序列滑动窗口
        MX_inc = cur_count = ori_count = 0
        for i in range(k):
            if strategy[i] == 1:
                ori_count += prices[i]
            elif strategy[i] == -1:
                ori_count -= prices[i]
            
            if i >= k // 2:
                cur_count += prices[i]

        MX_inc = max(0, cur_count - ori_count)

        left = 0
        ori_total = ori_count
        for right in range(k, len(strategy)):
            p = prices[right]
            s = strategy[right]
            
            if s == 1:
                ori_count += p
                ori_total += p
            elif s == -1:
                ori_count -= p
                ori_total -= p

            cur_count += p

            if strategy[left] == 1:
                ori_count -= prices[left]
            elif strategy[left] == -1:
                ori_count += prices[left]
            left += 1

            cur_count -= prices[right - k // 2]

            MX_inc = max(MX_inc, cur_count - ori_count)

        return ori_total + MX_inc   # 207ms



fmax = lambda x, y: x if x > y else y
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        total = max_diff = cur_diff = left = 0
        for right, (p, s) in enumerate(zip(prices, strategy)):
            total += p * s

            cur_diff += p * (1 - s)

            if right - left + 1 < k:
                if right >= k // 2 - 1:
                    cur_diff -= prices[right - k // 2 + 1]
                continue

            max_diff = fmax(max_diff, cur_diff)

            cur_diff -= prices[right - k // 2 + 1] - prices[left] * strategy[left]
            left += 1

        return total + max_diff


fmax = lambda x, y: x if x > y else y
class Solution:
    # 前缀和
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pre_li = list(accumulate((p * s for p, s in zip(prices, strategy)), initial=0))
        pre_p = list(accumulate(prices, initial=0))

        ans = pre_li[n]
        for i in range(k, n + 1):
            # 这里逻辑得捋清思路
            # 枚举修改子数组 [i−k,i−1]。修改后的利润由三部分组成：
            # [0,i−k−1] 的 prices[i]⋅strategy[i] 之和，即 sum[i−k]。
            # [i,n−1] 的 prices[i]⋅strategy[i] 之和，即 sum[n]−sum[i]。
            # [i−k/2,i−1] 的 prices[i] 之和，即 sumSell[i]−sumSell[i−k/2]。
            # 总和为
            # sum[i−k]+sum[n]−sum[i]+sumSell[i]−sumSell[i−k/2]
            cur = pre_li[i - k] + pre_li[n] - pre_li[i] + pre_p[i] - pre_p[i - k // 2]
            ans = fmax(ans, cur)

        return ans  # 251ms




fun = Solution()
fun.maxProfit([4,7,13], [-1,-1,0], 2)