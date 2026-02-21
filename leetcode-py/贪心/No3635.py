from math import inf
from typing import List


class Solution:
    # 暴力
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = inf
        for ls, ld in zip(landStartTime, landDuration):
            le = ls + ld
            if le >= ans:
                continue
            for ws, wd in zip(waterStartTime, waterDuration):
                if ws <= le:
                    ans = min(ans, le + wd)
                else:
                    ans = min(ans, ws + wd)

        for ws, wd in zip(waterStartTime, waterDuration):
            we = ws + wd
            if we >= ans:
                continue
            for ls, ld in zip(landStartTime, landDuration):
                if ls <= we:
                    ans = min(ans, we + ld)
                else:
                    ans = min(ans, ls + ld) # 可以观察到有结构上重复

        return ans  # 超时
    
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        le = min(x + y for x, y in zip(landStartTime, landDuration))
        we = min(x + y for x, y in zip(waterStartTime, waterDuration))
        ans = inf
        for ls, ld in zip(landStartTime, landDuration):
            ans = min(ans, max(we,ls) + ld)
        for ws, wd in zip(waterStartTime, waterDuration):
            ans = min(ans,max(le, ws) + wd)
        return ans  #194ms