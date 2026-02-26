
fmin = lambda x, y : y if x > y else x
fmax = lambda x, y : x if x > y else y
class Solution:
    # 贪心
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        if cost1 > cost2:
            cost1, cost2 = cost2, cost1
            need1, need2 = need2, need1

        if costBoth <= cost1 and costBoth <= cost2:
            return costBoth * fmax(need1, need2)
        
        if costBoth >= cost1 and costBoth >= cost2:
            return need1 * cost1 + need2 * cost2
        
        if cost1 <= costBoth <= cost2:
            MIN = fmin(need1, need2)
            return cost1 * fmax(0, need1 - MIN) + costBoth * MIN    # 错误


class Solution:
    # 贪心
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        if costBoth <= cost1 and costBoth <= cost2:
            return costBoth * fmax(need1, need2)
        
        if cost1 > cost2:
            cost1, cost2 = cost2, cost1
            need1, need2 = need2, need1
        
        ans = 0
        if need1 > need2:
            ans = cost1 * (need1 - need2) + costBoth * need2
        else:
            ans = cost2 * (need2 - need1) + costBoth * need1

        return min(ans, need1 * cost1 + need2 * cost2)  # 错误
    

class Solution:
    # 贪心
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        f1 = need1 * cost1 + need2 * cost2
        MIN = fmin(need1, need2)
        f2 = cost1 * (need1 - MIN) + cost2 * (need2 - MIN) + costBoth * MIN
        f3 = costBoth * fmax(need1, need2)
        return min(f1, f2, f3)
