from typing import List

# 注意题目最多只有一条出边
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        cur_time = 1
        vis_time = [0] * n
        for x in range(n):
            start_time = cur_time   
            while x != -1 and vis_time[x] == 0:
                vis_time[x] = cur_time
                cur_time += 1
                x = edges[x]
            if x != -1 and vis_time[x] >= start_time:
                ans = max(ans,cur_time - vis_time[x])

        return ans

