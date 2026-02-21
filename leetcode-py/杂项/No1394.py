from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for key, value in cnt.items():
            if key == value:
                ans = max(ans, key)
        return ans



