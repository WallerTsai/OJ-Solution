from typing import List


# 2026年5月12日 没想出来
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse= True)
        ans = cur = 0
        for a, b in tasks:
            ans = max(ans, cur + b)
            cur += a
        return ans