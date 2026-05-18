from math import inf
from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        for i, x in enumerate(documents):
            y = abs(x)
            if documents[y] < 0:
                return y
            documents[y] = -documents[y]    # 错误
            


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        for x in documents: 
            y = abs(x) if x != -inf else 0
            if documents[y] < 0:
                return y
            
            if documents[y] == 0:
                documents[y] = -inf
            else:
                documents[y] = -documents[y]


Solution().findRepeatDocument([2, 5, 3, 0, 5, 0])