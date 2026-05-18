from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)
        visited = set()
        visited.add(start)
        q = deque([start])
        while q :
            i = q.popleft()
            for j in [i - arr[i], i + arr[i]]:
                if 0 <= j < n and j not in visited:
                    if arr[j] == 0:
                        return True
                    q.append(j)
                    visited.add(j)
        return False