from typing import List


class Solution:
    # 三次遍历
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []

        left = [-1] * n # i 左侧小于 h 的最近元素下标
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        right = [n] * n # i 右侧小于 h 的最近元素下标
        st.clear()
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l -1))
        return ans  # 239ms
    

class Solution:
    # 两次遍历
    # 灵神

    # 把 right[i] 的定义略作修改，调整为：在 i 右侧的小于或等于 h=heights[i] 的最近元素的下标。

    # 如果 heights 中没有相同的元素，这样修改不影响 right[i]。

    # 如果 heights 中有相同的元素呢？比如 heights=[1,3,4,3,2]，左边那个 3 的 right[i] 会变小，导致矩形面积变小，这是否会导致计算错误？

    # 不会。注意在这种情况下，这两个高为 3 的柱子，对应的矩形面积（在写法一中）是一样大的，虽然（在写法二中）左边那个 3 的矩形面积变小了，但右边那个 3 的矩形面积是不变的，所以我们不会错过正确答案。

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        st = []
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans
    

class Solution:
    # 一次遍历
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