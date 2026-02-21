from collections import Counter, defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        for i, v in cnt.items():
            if i == v - 1:
                ans += v
            elif i < v - 1:
                ans += (i + 1) * ((v - 1) // (i + 1)) + i + 1
            else:
                ans += i + 1
        return ans 


class Solution:
    # 灵神
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        left = defaultdict(int)
        for x in answers:
            if left[x] == 0:
                ans += x + 1  # 找到了一个大小为 x+1 的颜色组
                left[x] = x  # 允许其他 x 只兔子也回答 x
            else:
                left[x] -= 1
        return ans





