from collections import Counter
from typing import List

# 由于 digits 可能很多，所以建议枚举每位数（0 - 10）
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        res = []

        def dfs(i: int, cur_num: int) -> None:
            if i == 2:
                for num in range(0,10,2):
                    if cnt[num] > 0:
                        res.append(cur_num * 10 + num)
                return
            
            start_num = 1 if i == 0 else 0

            for num in range(start_num, 10):
                if cnt[num] > 0:
                    cnt[num] -= 1
                    dfs(i + 1, cur_num * 10 + num)
                    # 恢复现场
                    cnt[num] += 1
            
        dfs(0, 0)
        return res



