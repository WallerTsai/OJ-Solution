from bisect import bisect_right
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s:str):
            return s.count(min(s))
        fword = sorted( f(word) for word in words)
        res,length = [],len(words)
        for query in queries:
            index = bisect_right(fword,f(query))
            res.append(length-index)
        return res  # 7ms

class Solution:
    # 使用前缀和优化掉排序和二分查找
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s:str):
            return s.count(min(s))
        cnt = [0] * 11 # 需要多出一个
        res = []
        # 计数
        for word in words:
            cnt[f(word)-1] += 1
        # 前缀和
        for i in range(8,-1,-1):
            cnt[i] += cnt[i+1]
        # 统计结果
        for query in queries:
            res.append(cnt[f(query)])
        return res  # 3ms