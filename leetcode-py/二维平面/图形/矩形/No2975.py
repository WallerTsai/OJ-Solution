from itertools import combinations
from typing import List, Set


MOD = 1_000_000_007
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        x_set = set()
        vFences.extend([1, n])
        for i in range(1, len(vFences)):
            for j in range(i):
                x_set.add(abs(vFences[i] - vFences[j]))

        y_set = set()
        hFences.extend([1, m])
        for i in range(1, len(hFences)):
            for j in range(i):
                y_set.add(abs(hFences[i] - hFences[j]))

        intersection_set = x_set & y_set
        
        return pow(max(intersection_set), 2) % MOD if intersection_set else -1


class Solution:
    def f(self, a: List[int], mx: int) -> Set[int]:
        a += [1, mx]
        a.sort()
        # 计算 a 中任意两个数的差，保存到哈希集合中
        return set(y - x for x, y in combinations(a, 2))

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 1_000_000_007
        h_set = self.f(hFences, m)
        v_set = self.f(vFences, n)

        ans = max(h_set & v_set, default=0)
        return ans * ans % MOD if ans else -1