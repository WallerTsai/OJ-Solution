from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(1,len(A)+1):
            length = len(set(A[:i]) & set(B[:i]))
            res.append(length)
        return res  # 40ms


class Solution:
# 作者：灵茶山艾府
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        ans = []
        p = q = 0
        for x, y in zip(a, b):
            p |= 1 << x
            q |= 1 << y
            ans.append((p & q).bit_count())
        return ans

