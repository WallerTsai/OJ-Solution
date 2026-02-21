from collections import defaultdict
from typing import Dict, List


class Solution:
    # 灵神
    def calc_amount(self, pairs: List[List[str]], rates: List[float], initialCurrency: str) -> Dict[str, float]:
        g = defaultdict(list)
        for (x, y), r in zip(pairs, rates):
            g[x].append((y, r))
            g[y].append((x, 1.0 / r))

        amount = {}
        def dfs(x: str, cur_amount: float) -> None:
            amount[x] = cur_amount
            for to, rate in g[x]:
                # 每个节点只需递归一次（重复递归算出来的结果是一样的，因为题目保证汇率没有矛盾）
                if to not in amount:
                    dfs(to, cur_amount * rate)
        dfs(initialCurrency, 1.0)
        return amount

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        day1_amount = self.calc_amount(pairs1, rates1, initialCurrency)
        day2_amount = self.calc_amount(pairs2, rates2, initialCurrency)
        return max(day1_amount.get(x, 0.0) / a2 for x, a2 in day2_amount.items())

