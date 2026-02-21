from heapq import heappop, heappush, heappushpop
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l = sorted(((i,x,y) for i, (x,y) in enumerate(zip(nums1,nums2))),key=lambda z :z[1])
        n = len(l)
        ans = [0] * n
        hq = []
        cur_sum = 0
        for _,(index,x,y) in enumerate(l):
            ans[index] = cur_sum
            cur_sum += y
            heappush(hq,y)
            if len(l) > k:
                cur_sum -= heappop(hq)
        return ans
        # 错误，注意相同
    
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l = sorted(((i,x,y) for i, (x,y) in enumerate(zip(nums1,nums2))),key=lambda z :z[1])
        n = len(l)
        ans = [0] * n
        hq = []
        cur_sum = 0
        for i,(index,x,y) in enumerate(l):
            ans[index] = ans[l[i-1][0]] if i and x == l[i-1][1] else cur_sum
            cur_sum += y
            heappush(hq,y)
            if len(hq) > k:
                cur_sum -= heappop(hq)
        return ans

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))
        n = len(a)
        ans = [0] * n
        h = []
        s = 0
        for i, (x, y, idx) in enumerate(a):
            ans[idx] = ans[a[i - 1][2]] if i and x == a[i - 1][0] else s
            s += y
            if len(h) < k:
                heappush(h, y)
            else:
                s -= heappushpop(h, y)
        return ans