from functools import reduce
from operator import xor
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cur = pre = 0
        for n in derived:
            cur ^= n
        return cur == pre
    
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0