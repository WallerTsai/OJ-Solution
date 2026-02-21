from collections import defaultdict
from typing import Counter, List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter()
        li1, li2 = list(), list()
        for num in basket2:
            if not cnt1[num]:
                cnt2[num] += 1
                continue
            cnt1[num] -= 1
        for num, count in cnt1.items():
            if not count:
                continue
            if count % 2:
                return -1
            li1.extend([num] * (count // 2))
        for num, count in cnt2.items():
            if not count:
                continue
            if count % 2:
                return -1
            li2.extend([num] * (count // 2))
            

        li1.sort()
        li2.sort(reverse=True)
        
        ans = 0
        n, m = len(li1), len(li2)
        if not (n == m):
            return -1
        for num1, num2 in zip(li1, li2):
            ans += min(num1, num2)
        
        return ans  # 错误

fun = Solution()
fun.minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8])

print(sorted([84,80,43,8,80,88,43,14,100,88]), sorted([32,32,42,68,68,100,42,84,14,8]), sep= '\n')

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter()
        
        for num in basket2:
            if not cnt1[num]:
                cnt2[num] += 1
                continue
            cnt1[num] -= 1

        MIN = min(basket1 + basket2)

        ans = n1 = n2 = 0
        for num, count in cnt1.items():
            if count % 2:
                return -1
            n1 += count // 2
            if num != MIN:
                ans  += MIN * (count // 2)

        for num, count in cnt2.items():
            if count % 2:
                return -1
            n2 += count // 2
            if num != MIN:
                ans  += MIN * (count // 2)

        return ans if n1 == n2 else -1  # 错误
        [4,4,4,4,3]
        [5,5,5,5,3]

class Solution:
    # 灵神
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1

        a = []
        for x, c in cnt.items():
            if c % 2:
                return -1
            a.extend([x] * (abs(c) // 2))

        a.sort()
        mn = min(cnt)

        return sum(min(x, mn * 2) for x in a[:len(a) // 2])