from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        ans = cnt = 0
        day = 1
        n = len(pizzas)
        index = n - 1
        while cnt < n:
            ans += pizzas[index]
            if day % 2 == 1:
                index -= 2
            else:
                index -= 1
            day += 1
            cnt += 4
        return ans


class Solution:
    # 不应该是dp
    # 先贪奇数天，再贪偶数天
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        days = len(pizzas) // 4
        odd = (days+1) // 2
        # 先选奇数天
        sum_odd  = sum(pizzas[:odd])
        # 再选偶数天
        sum_even = sum(pizzas[odd+1:odd+days//2 * 2 + 1:2])
        
        return sum_odd + sum_even # 182ms
    
    # 证明交换论证法

class Solution:
    # 不应该是dp
    # 先贪奇数天，再贪偶数天
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        days = len(pizzas) // 4
        odd = (days+1) // 2
        # 先选奇数天
        sum_odd  = sum(pizzas[:odd])
        # 再选偶数天
        sum_even = sum(pizzas[odd+1:odd+days//2 * 2:2])
        
        return sum_odd + sum_even