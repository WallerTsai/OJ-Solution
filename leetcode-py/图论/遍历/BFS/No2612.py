from collections import deque
from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban = set(banned)
        sets = [SortedList(), SortedList()] # 有序列表维护奇偶

        for i in range(n):
            if i != p and i not in ban:
                sets[i % 2].add(i)
        
        ans = [-1] * n
        ans[p] = 0

        # BFS
        q = deque()
        q.append(p)
        while q:
            i = q.popleft()
            mn = max(i - k + 1, k - i -1)
            mx = min(i + k - 1, 2 * n - k - i -1)
            target_set = sets[mx % 2]
            to_romove = []
            for val in target_set.irange(mn, mx):
                ans[val] = ans[i] + 1
                q.append(val)
                to_romove.append(val)
            for val in to_romove:
                target_set.remove(val)
        return ans



