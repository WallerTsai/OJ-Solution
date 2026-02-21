from itertools import accumulate
from typing import List

# KPM + 差分
class Solution:

    def bulid_PMT(self,pattern:str,L:int) ->List[int]:
        #生成部分匹配表
        pmt = [0] * L       # 初始化PMT
        length = 0          # 记录当前最长前缀长度

        # pmt[0] = 0
        for i in range(1,L):
            while length > 0 and pattern[i] != pattern[length]:
                length = pmt[length-1]
            if pattern[i] == pattern[length]:
                length += 1
            pmt[i] = length

        return pmt


    def KPM_to_diff_array(self, text: list, needle: str) -> int:
        #KMT字符串匹配算法
        l1,l2 = len(text),len(needle)

        pmt = self.bulid_PMT(pattern=needle,L=l2)   #生成pmt表

        j = 0       #记录needle的下标指针

        diff = [0] * (l1 + 1)
        for i in range(l1):

            while j > 0 and text[i] != needle[j]:
                j = pmt[j-1]        #寻找前一个字符的pmt值

            if text[i] == needle[j]:
                j += 1

            if j == l2:             
                diff[i - l2 + 1] += 1
                diff[i + 1] -= 1
                j = pmt[j - 1]

        return list(accumulate(diff))

    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        h_text = [c for row in grid for c in row]
        v_text = [c for col in zip(*grid) for c in col]

        in_pattern_h = self.KPM_to_diff_array(h_text, pattern)
        in_pattern_v = self.KPM_to_diff_array(v_text, pattern)


        m, n = len(grid), len(grid[0])
        ans = 0
        for i, in_h in enumerate(in_pattern_h):
            if in_h and in_pattern_v[i % n * m + i // n]:   # 注意这个下标转换关系
                ans += 1
        return ans


# KMP + 合并区间
class Solution:
    def bulid_PMT(self,pattern:str,L:int) ->List[int]:
        #生成部分匹配表
        pmt = [0] * L       # 初始化PMT
        length = 0          # 记录当前最长前缀长度

        # pmt[0] = 0
        for i in range(1,L):
            while length > 0 and pattern[i] != pattern[length]:
                length = pmt[length-1]
            if pattern[i] == pattern[length]:
                length += 1
            pmt[i] = length

        return pmt


    def KPM_to_diff_array(self, text: list, needle: str) -> int:
        #KMT字符串匹配算法
        l1,l2 = len(text),len(needle)

        pmt = self.bulid_PMT(pattern=needle,L=l2)   #生成pmt表

        j = 0       #记录needle的下标指针

        res = []
        for i in range(l1):

            while j > 0 and text[i] != needle[j]:
                j = pmt[j-1]        #寻找前一个字符的pmt值

            if text[i] == needle[j]:
                j += 1

            if j == l2:             
                res.append([i - l2 + 1, i])
                j = pmt[j-1]

        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        return ans
    
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        h_text = [c for row in grid for c in row]
        v_text = [c for col in zip(*grid) for c in col]

        in_pattern_h = self.merge(self.KPM_to_diff_array(h_text, pattern))
        in_pattern_v = self.merge(self.KPM_to_diff_array(v_text, pattern))

        m, n = len(grid), len(grid[0])
        visited = set()

        for l, r in in_pattern_h:
            for x in range(l,r + 1):
                i, j = divmod(x,n)
                visited.add((i,j))

        ans = 0
        for l, r in in_pattern_v:
            for x in range(l, r + 1):
                j, i = divmod(x, m)
                if (i, j) in visited:
                    ans += 1
                    
        return ans

    
    