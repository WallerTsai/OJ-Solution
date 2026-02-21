from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])
        for i in range(1,len(items)):
            items[i][1] = max(items[i][1],items[i-1][1])
        for i, q in enumerate(queries):
            index = bisect_right(items,q,key=lambda x:x[0])
            queries[i] = items[index-1][1] if index else 0
        return queries