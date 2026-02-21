from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        i = 0
        for a, b, c, m in variables:
            if pow((pow(a, b) % 10), c) % m == target:
                res.append(i)
            i += 1
        return res

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow((pow(a, b, 10)), c, m) == target:
                res.append(i)
        return res  # 3ms
