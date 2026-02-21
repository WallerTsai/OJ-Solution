from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        idx = sorted(range(n),key= lambda x:difficulty[x])
        MX_profit = 0
        ans = index = 0
        for wo in sorted(worker):
            while index < n and wo >= difficulty[idx[index]]:
                MX_profit = max(MX_profit, profit[idx[index]])
                index += 1
            ans += MX_profit
        return ans 
            
            