from collections import defaultdict
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans = ""
        cnt = defaultdict(int)
        count = 0
        for l in responses:
            for a in set(l):
                cnt[a] += 1
                if cnt[a] > count:
                    count = cnt[a]
                    ans = a
                elif cnt[a] == count:
                    if a < ans:
                        ans = a
        return ans