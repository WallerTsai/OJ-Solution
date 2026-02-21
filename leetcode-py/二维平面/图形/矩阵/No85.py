# 调用 No84题 代码解决


from typing import List


class Solution:
    # No84
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 前后哨兵
        heights = [0] + heights + [0]
        
        st = []
        ans = 0

        for right, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                i = st.pop(-1)  # 矩阵的高 下标
                left = st[-1]
                ans = max(ans, heights[i] * (right - left - 1))
            st.append(right)

        return ans
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for i, c in enumerate(row):
                if c == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans  # 31ms
    


# 2026年1月11日
fmax = lambda x, y : x if x > y else y
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # O(1)
        st = [-1]
        ans = 0
        for right, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                i = st.pop(-1)
                left = st[-1]
                ans = fmax(ans, heights[i] * (right - left -1))
            st.append(right)
        
        return ans
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for i, ch in enumerate(row):
                if ch == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            ans = fmax(ans, self.largestRectangleArea(heights[:]))  # 注意调用副本，不然调用函数heights长度+1

        return ans
    

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0

        for row in matrix:
            for i, ch in enumerate(row):
                heights[i] = heights[i] + 1 if ch == '1' else 0

            st = [-1]
            for right, h in enumerate(heights):
                while st[-1] != -1 and heights[st[-1]] > h:
                    height = heights[st.pop(-1)]
                    left = st[-1]
                    if height * (right - left - 1) > ans:
                        ans = height * (right - left - 1)
                st.append(right)
                
        return ans  # 25ms


