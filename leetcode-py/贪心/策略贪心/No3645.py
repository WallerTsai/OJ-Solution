from collections import defaultdict
from typing import List


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        ans = 0
        li = list()
        cnt = defaultdict(int)
        for v, l in zip(value, limit):
            li.append((l, -v))
            cnt[l] += 1
        li.sort()
        active_num = inactive_limit = 0
        for l, v in li:
            if l == inactive_limit:
                continue
            if active_num >= l:
                break
            ans -= v
            active_num += 1
            if cnt[active_num]:
                inactive_limit = active_num
                temp = cnt[active_num]
                del cnt[active_num]
                active_num -= temp
                active_num = max(active_num, 0)
        return ans
    
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        d=defaultdict(list)
        for v,l in zip(value,limit):
            d[l].append(v)
        res=0
        for l,vl in d.items():
            vl.sort()
            res+=sum(vl[-l:])
        return res
    
fun = Solution()
fun.maxTotal([35691,69137,45902,3205,79614],[2,2,2,1,3])

print([1,2,3,4][-2:])