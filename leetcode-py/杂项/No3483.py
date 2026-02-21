from itertools import permutations
from typing import List


# class Solution:
#     def totalNumbers(self, digits: List[int]) -> int:
#         even_number = 0
#         zero_in = False
#         for x in digits:
#             if x % 2 == 0:
#                 if x == 0:
#                     zero_in = True
#                 even_number += 1
#         n = len(digits)

#         ans = even_number * (n - 1) * (n - 2)
        # 不对

# 只能暴力了
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans_set = set()
        for a,b,c in permutations(digits,3):
            if a != 0 and (c % 2) == 0:
                ans_set.add((a,b,c)) 
        return len(ans_set) # 13ms

