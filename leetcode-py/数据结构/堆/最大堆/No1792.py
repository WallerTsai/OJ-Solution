import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        nums = [[x / y, x, y] for x, y in classes]
        heapq.heapify(nums)
        for i in range(extraStudents):
            _, x, y = heapq.heappop(nums)
            heapq.heappush(nums, [(x + 1) / (y + 1), x + 1, y + 1])

        return sum([avg for avg, _, _ in nums]) / n # 思路错误
    # 给通过率最低的班加学霸不是最优策略

# 最优策略应该是给 (x + 1) / (y + 1) - x / y 的最大值所在班里加学霸

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        hq = []
        for x, y in classes:
            increase = (x + 1) / (y + 1) - x / y
            heapq.heappush(hq,(-increase, x, y))

        for _ in range(extraStudents):
            _, x, y = heapq.heappop(hq)
            x += 1
            y += 1
            new_increase = (x + 1) / (y + 1) - x / y
            heapq.heappush(hq, (-new_increase, x, y))

        total = 0
        for _, x, y in hq:
            total += x / y

        return total / n    # 1209ms