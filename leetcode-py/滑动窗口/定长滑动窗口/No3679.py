from collections import defaultdict
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        ans = left = count = 0
        pop_set = set()
        for right, num in enumerate(arrivals):
            cnt[num] += 1
            count += 1
            while count > w:
                if left not in pop_set:
                    cnt[arrivals[left]] -= 1
                    count -= 1
                left += 1
            if cnt[num] > m:
                pop_set.add(right)
                cnt[num] -= 1
                count -= 1
                ans += 1


        return ans  # 错误


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        ans = left  = 0
        pop_set = set()
        for right, num in enumerate(arrivals):
            cnt[num] += 1
            if right - left + 1 > w:
                if left not in pop_set:
                    cnt[arrivals[left]] -= 1
                left += 1
            if cnt[num] > m:
                pop_set.add(right)
                cnt[num] -= 1
                ans += 1

        return ans
    

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i, x in enumerate(arrivals):
            if cnt[x] == m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[x] += 1
            
            left = i - w + 1
            if left >= 0:
                cnt[arrivals[left]] -= 1
        
        return ans