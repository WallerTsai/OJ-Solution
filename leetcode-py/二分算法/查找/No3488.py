from bisect import bisect_left
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        cnt = defaultdict(list)
        for i, x in enumerate(nums):
            cnt[x].append(i)
        n = len(nums)
        ans = []
        for q in queries:
            t = nums[q]
            if len(cnt[t]) == 1:
                ans.append(-1)
                continue
            idx = bisect_left(cnt[t], q)
            d = inf
            d = min(d, 
                    abs(q - cnt[t][(idx + 1) % len(cnt[t])]), 
                    abs(q - cnt[t][idx - 1]),
                    n - abs(q - cnt[t][(idx + 1) % len(cnt[t])]),
                    n - abs(q - cnt[t][idx - 1])
                    )
            ans.append(d if d != inf else -1)
        return ans
            
# 以下为灵神解法
class Solution:
    # 哨兵
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, x in enumerate(nums):
            indices[x].append(i)

        n = len(nums)
        for p in indices.values():
            # 前后各加一个哨兵
            i0 = p[0]
            p.insert(0, p[-1] - n)
            p.append(i0 + n)

        for qi, i in enumerate(queries):
            p = indices[nums[i]]
            if len(p) == 3:
                queries[qi] = -1
            else:
                j = bisect_left(p, i)
                queries[qi] = min(i - p[j - 1], p[j + 1] - i)
        return queries

class Solution:
    # 左右链表
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        first = {}  # 记录首次出现的位置
        last = {}  # 记录最后一次出现的位置
        for i, x in enumerate(nums):
            left[i] = j = last.get(x, -1)
            if j >= 0:
                right[j] = i
            if x not in first:
                first[x] = i
            last[x] = i

        for qi, i in enumerate(queries):
            l = left[i] if left[i] >= 0 else last[nums[i]] - n
            if i - l == n:
                queries[qi] = -1
            else:
                r = right[i] or first[nums[i]] + n
                queries[qi] = min(i - l, r - i)
        return queries



