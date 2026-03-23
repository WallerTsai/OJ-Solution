from typing import List

# 寻找入度为0的节点集合
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        endSet = set(y for x, y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans



