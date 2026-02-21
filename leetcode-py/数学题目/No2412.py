from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 先求最大亏损
        max_lost = 0
        for cost,back in transactions:
            if cost > back:
                max_lost += cost - back
        # 再找亏完后,最大开销的赚钱项
        max_cost = 0
        for cost,back in transactions:
            if cost <= back:
                max_cost = max(max_cost,cost)
        
        return max_lost + max_cost  # 错误 如果没有赚钱项则错
    


    # 题目不应该是求 最大亏损+再找亏完后,最大开销的赚钱项
    # 而是求你 最穷的时刻，需要多少钱：
    # 对于赚钱项:假设你的第一笔赚钱项，那么你需要你亏完钱后，再花费cost才可以赚钱 (这行分析不对)
    # 如果你不只有一个赚钱项，你需要找到最大的cost,这时候就是你最穷最坏的情况
    # 对于只有亏钱项目:那么就是你最大那笔back没有回到手的时候你最穷，
    # 也就是说你投资的最后一笔一定是最大的back (有点难理解这里)
    # 可以反过来思考,如果你不得不投资一部分亏钱项目，正常人都会在力所能及的条件下投资回报最多的那个
    # 这样就可以缓解一下资金压力
    # 这道题算是数学题了
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        max_lost = 0
        for cost,back in transactions:
            if cost > back:
                max_lost += cost - back
        max_back = max_cost = 0
        for cost,back in transactions:
            if cost <= back:
                max_cost = max(max_cost,cost)
            else:
                max_back = max(max_back,back)
        
        if max_cost:
            return max_lost + max_cost
        else:
            return max_lost + max_back # 在统计 max_lost 已经减去，则补回来
        # 错误 还有点小细节

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        max_lost = 0
        for cost,back in transactions:
            if cost > back:
                max_lost += cost - back
        max_back = max_cost = 0
        for cost,back in transactions:
            if cost <= back:
                max_cost = max(max_cost,cost)
            else:
                max_back = max(max_back,back)
        # 如果最后一笔亏本项的back大于最大的赚钱项目,那么最穷的时候应该是back没回来
        return max_lost + max(max_cost,max_back)    # 43ms
    
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        max_lost = MAX = 0
        for cost,back in transactions:
            if cost > back:
                max_lost += cost - back
                if MAX < back:
                    MAX = back
            else:
                if MAX < cost:
                    MAX = cost
        return max_lost + MAX   # 5ms