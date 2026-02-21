from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        li = deque()
        s = set()
        for i, r in enumerate(rains):
            if r == 0:
                li.append(i)
                continue

            if r not in s:
                s.add(r)
            else:
                if not li:
                    return []
                else:
                    index = li.popleft()
                    ans[index] = r

        return ans  # 错误



class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        li = []
        s = dict()
        for i, r in enumerate(rains):
            if r == 0:
                li.append(i)
                continue

            if r not in s:
                s[r] = i
            else:
                if not li:
                    return []
                else:
                    index = bisect_left(li, s[r])
                    if index == len(li):
                        return []
                    ans[li[index]] = r
                    s[r] = i
                    li.pop(index)
        if li:
            for i in li:
                ans[i] = 1
                
        return ans  # 274ms
    

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        # 非递归并查集
        fa = list(range(n + 1))
        def find(x: int) -> int:
            rt = x
            while fa[rt] != rt:
                rt = fa[rt]
            while fa[x] != rt:
                fa[x], x = rt, fa[x]
            return rt

        ans = [-1] * n
        full_day = {}  # lake -> 装满日
        for i, lake in enumerate(rains):
            if lake == 0:
                ans[i] = 1  # 先随便选一个湖抽干
                continue
            if lake in full_day:
                j = full_day[lake]
                # 必须在 j 之后，i 之前把 lake 抽干
                # 选一个最早的未被使用的抽水日，如果选晚的，可能会导致其他湖没有可用的抽水日
                dry_day = find(j + 1)
                if dry_day >= i:
                    return []  # 无法阻止洪水
                ans[dry_day] = lake
                fa[dry_day] = find(dry_day + 1)  # 删除 dry_day
            fa[i] = i + 1  # 删除 i
            full_day[lake] = i  # 插入或更新装满日
        return ans  # 97ms