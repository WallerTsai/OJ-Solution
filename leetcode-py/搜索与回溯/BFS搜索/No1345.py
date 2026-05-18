from collections import defaultdict
from itertools import count
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        cnt = defaultdict(list)
        for i, x in enumerate(arr):
            cnt[x].append(i)

        visited = set()
        visited.add(0)
        q = [0]

        for ans in count(0):
            nxq = []

            for i in q:
                if i == n - 1:
                    return ans
                
                if i + 1 < n and i + 1 not in visited:
                    visited.add(i + 1)
                    nxq.append(i + 1)
                
                if i - 1 >= 0 and i - 1 not in visited:
                    visited.add(i - 1)
                    nxq.append(i - 1)

                for idx in cnt[arr[i]]:
                    if idx not in visited:
                        visited.add(idx)
                        nxq.append(idx)

                cnt.pop(arr[i])

            q = nxq
        
        return -1



