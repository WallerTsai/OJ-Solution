from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        pre_end = 0
        ans = 0
        for s, e in meetings:
            if s > pre_end + 1:
                ans += s - pre_end - 1
            pre_end = max(pre_end, e)
        ans += days - pre_end
        return ans  # 95ms