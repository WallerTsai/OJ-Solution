from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # lambda x : (x.bit_count(),x) 这里的意思是如果第一个条件比较失效，那就采用本身值大小来排序
        return sorted(arr,key=lambda x : (x.bit_count(),x)) # 0-3ms


