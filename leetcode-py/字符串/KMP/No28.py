# 模板题
from typing import List


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


    def strStr(self, haystack: str, needle: str) -> int:
        #KMT字符串匹配算法
        l1,l2 = len(haystack),len(needle)

        pmt = self.bulid_PMT(pattern=needle,L=l2)   #生成pmt表

        j = 0       #记录needle的下标指针

        #开始遍历
        for i in range(l1):

            while j > 0 and haystack[i] != needle[j]:
                j = pmt[j-1]        #寻找前一个字符的pmt值

            if haystack[i] == needle[j]:
                j += 1

            if j == l2:             #匹配完毕
                return i-l2+1

        return -1                   #找不到匹配返回-1
        