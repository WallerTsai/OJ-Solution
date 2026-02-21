from bisect import bisect_left
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits,startPos-k,key=lambda x:x[0])
        res = cnt = 0
        for pos,num in fruits[left:]:
            if pos > startPos + k:
                break
            cnt += num
            # 先右后左，右路程为两倍，先左后右同理
            while pos - fruits[left][0] + pos - startPos > k and pos - fruits[left][0] + startPos - fruits[left][0] > k:
                cnt -= fruits[left][1]
                left += 1
            res = max(res,cnt)
        return res


