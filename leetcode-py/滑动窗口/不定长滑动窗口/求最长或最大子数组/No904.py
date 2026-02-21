from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = left = cnt = 0
        dd = defaultdict(int)

        for right,num in enumerate(fruits):
            if num not in dd:
                cnt += 1
            dd[num] += 1
            while cnt > 2:
                dd[fruits[left]] -= 1
                if dd[fruits[left]] == 0:
                    cnt -= 1
                    dd.pop(fruits[left])
                left += 1
            res = max(res,right-left+1)
        return res  # 215ms
    
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = left = 0
        for right in range(len(fruits)+1):
            while len(set(fruits[left:right])) > 2:
                left += 1

            res = max(res,right-left)
        return res # 超时
    
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits)) == 1:
            return len(fruits)
        left = 0
        for right in range(len(fruits)+1):
            if len(set(fruits[left:right])) > 2:
                left += 1

        return right - left # 超时

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = cnt = 0
        dd = defaultdict(int)

        for right,num in enumerate(fruits):
            if num not in dd:
                cnt += 1
            dd[num] += 1
            if cnt > 2:
                dd[fruits[left]] -= 1
                if dd[fruits[left]] == 0:
                    cnt -= 1
                    dd.pop(fruits[left])
                left += 1

        return right - left + 1 # 135ms



