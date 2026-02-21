from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        left,right = 0,length
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= length - mid:
                right = mid
            else:
                left = mid + 1
        return length-left  
        # 这个思路难理解

class Solution:
    # 灵神思路
    def hIndex(self, citations: List[int]) -> int:
        # 在区间 [left, right) 内询问
        left = 1
        right = len(citations) + 1
        while left < right:  # 区间不为空
            # 循环不变量：
            # left-1 的回答一定为「是」
            # right 的回答一定为「否」
            mid = (left + right) // 2
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid + 1  # 询问范围缩小到 [mid+1, right)
            else:
                right = mid  # 询问范围缩小到 [left, mid)
        # 根据循环不变量，left-1 现在是最大的回答为「是」的数
        return left - 1