from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        heights = [0] + heights + [0]
        st = []
        ans = 0
        for right, h in enumerate(heights):
            # 假设当前柱子已经是最小的一边了
            while st and heights[st[-1]] > h:
                # 这个柱子的左右两个边界都比他小
                cur_idx = st.pop()
                cur_height = heights[cur_idx]

                left = st[-1]
                cur_width = right - left - 1    # 对宽度的贡献
                ans = max(ans, cur_width * cur_height)

            st.append(right)

        return ans



