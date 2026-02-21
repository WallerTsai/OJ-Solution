from bisect import bisect_left
from typing import List


class Solution:
    # 前缀和 + 二分查找
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        C = [0]
        R = [0]
        H = [0]
        for c,r,h in increase:
            C.append(C[-1]+c)
            R.append(R[-1]+r)
            H.append(H[-1]+h)
        res = []
        length = len(C)
        for c_,r_,h_ in requirements:
            t1 = bisect_left(C,c_)
            t2 = bisect_left(R,r_)
            t3 = bisect_left(H,h_)
            
            t = max(t1,t2,t3)
            if t == length:
                res.append(-1)
            else:
                res.append(t)
        return res  # 261ms
            