# 难度中等
from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        freq = list(Counter(arr).values())
        freq.sort(reverse=True)
        cur_length = 0
        for i,value in enumerate(freq,1):
            cur_length += value
            if cur_length >= (length+1) //2 :
                return i

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        freq = list(Counter(arr).values())
        freq.sort(reverse=True)
        cur_length = 0
        for i,value in enumerate(freq,1):
            cur_length += value
            if 2 * cur_length >= length :
                return i