import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        limit = (k-1) // n + 1
        nums = []
        for row,row_list in enumerate(matrix):
            nums.extend(row_list[:limit])
        nums.sort()
        return nums[k]  # 逻辑错误

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        hq = [(matrix[row][0],row,0) for row in range(n)]

        heapq.heapify(hq)

        for _ in range(k-1):
            num ,row , index = heapq.heappop(hq)
            if index != n - 1:
                heapq.heappush(hq,(matrix[row][index+1],row,index+1))
        
        return heapq.heappop(hq)[0]


class Solution:
    # 作者：mkdir700
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            """遍历获取较小元素部分元素总数，并与k值比较"""
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    # 当前元素小于mid，则此元素及上方元素均小于mid
                    num += i + 1
                    # 向右移动
                    j += 1
                else:
                    # 当前元素大于mid，则向上移动，直到找到比mid小的值，或者出矩阵
                    i -= 1
            return num >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                # 满足 num >= k，范围太大，移动right至mid， 范围收缩
                right = mid
            else:
                left = mid + 1
        return left