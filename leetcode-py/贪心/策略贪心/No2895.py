from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = -1
        for i, x in enumerate(processorTime):
            ans = max(ans,x + tasks[i*4])
        return ans