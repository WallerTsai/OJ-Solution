from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_arr = [0]
        for a in arr:
            pre_arr.append(a ^ pre_arr[-1])
        ans = []
        for l, r in queries:
            ans.append(pre_arr[r + 1] ^ pre_arr[l])
        return ans  # 19ms
    
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = [0] + list(accumulate(arr, xor))
        return [prexor[q[1] + 1] ^ prexor[q[0]] for q in queries]