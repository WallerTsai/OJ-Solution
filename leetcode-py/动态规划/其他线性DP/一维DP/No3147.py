from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf
        for i in range(k):
            total = sum(energy[j] for j in range(i, len(energy), k))
            ans = max(ans, total)
        return ans  # 错误
    
    
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = -inf
        for i in range(n - k, n):  # 枚举终点 i
            suf_sum = accumulate(energy[j] for j in range(i, -1, -k))  # 计算后缀和
            ans = max(ans, max(suf_sum))
        return ans

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
    
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        res = [0] * length
        for i in range(length - 1, length - k - 1, -1):
            res[i] = energy[i]
        for i in range(length - k - 1, -1, -1):
            res[i] = res[i + k] + energy[i]
        return max(res)