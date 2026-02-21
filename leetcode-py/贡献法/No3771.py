from bisect import bisect_left
from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        li = [0]
        n = len(damage)
        ans = l_ptr = r_ptr = 0
        for i in range(n - 1, -1, -1):
            d = damage[i]
            r = requirement[i]
            l = hp - d

            while l_ptr < r_ptr:
                if li[r_ptr] - li[l_ptr] + requirement[n - l_ptr - 1] > l:
                    l_ptr += 1
                else:
                    break
            
            li.append(damage[i] + li[-1])
            r_ptr += 1
            if l < r:
                l_ptr = r_ptr
                continue
            ans += r_ptr - l_ptr

        return ans  # 错在 用例968
    
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        damage = damage[::-1]
        requirement = requirement[::-1]
        pre_sum_damage = list(accumulate(damage, initial=0))
        ans = left = 0
        for i in range(n):
            d, r = damage[i], requirement[i]
            l = hp - d
            if l < r:
                left = i
                continue

            while left < i and pre_sum_damage[i] - pre_sum_damage[left] + requirement[left] > l:
                left += 1
            
            ans += i - left + 1

        return ans  # 同上
    

# 正确的优化思路：贡献度法
# 与其计算每个起始点的总分，不如计算每个房间 i 对总分的贡献。即：有多少个起始点 j in [1, i] 能够让玩家在房间 i 拿到分数？
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        s = list(accumulate(damage, initial=0))

        ans = 0
        for i in range(n):
            # s[j-1] >= s[i+1] + requirement[i] - hp
            target = s[i + 1] + requirement[i] - hp

            if target <= 0:
                ans += i + 1
            else:
                idx = bisect_left(s, target, 0, i + 1)
                ans += i - idx + 1
        
        return ans  # 158ms

        
    
fun = Solution()
fun.totalScore(11,[3,6,7],[4,2,5])
            



