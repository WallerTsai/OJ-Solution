from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans = 0
        tail = weight[-1]
        for i in range(len(weight) - 2, -1 ,-1):
            if weight[i] > tail:
                ans += 1
                if i:
                    tail = weight[i - 1]
            else:
                tail = weight[i]
        return ans



