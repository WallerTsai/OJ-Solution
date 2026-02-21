from collections import defaultdict
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        endTime = [0] + endTime
        startTime = startTime + [eventTime]
        li = list(zip(endTime,startTime))
        
        # 后缀最大值
        n = len(startTime)
        suf_list = defaultdict(int)
        suf_max = 0
        for i in range(n - 1, -1, -1):
            e, s = li[i]
            suf_list[s] = suf_max
            suf_max = max(suf_max, s - e )

        ans = 0
        pre_max = 0
        pre_l, pre_r = li[0]
        for i in range(1, n):
            cur_l, cur_r = li[i]
            space = (pre_r - pre_l) + (cur_r - cur_l)
            need = cur_l - pre_r
            if need <= pre_max or need <= suf_list[cur_r]:
                space += need
            ans = max(ans, space)

            pre_max = max(pre_max, pre_r - pre_l)
            pre_r = cur_r
            pre_l = cur_l

        return ans  # 296ms


fun = Solution()
fun.maxFreeTime(10, [0,3,7,9], [1,4,8,10])