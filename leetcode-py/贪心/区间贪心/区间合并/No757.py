from collections import defaultdict
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        nums = []
        intervals.sort(key=lambda x: x[1])
        pre_2, pre_1 = -1, -1
        for l, r in intervals:
            if l > pre_1:
                if l != r:
                    nums.extend([r - 1, r])
                    pre_2, pre_1 = r - 1, r
                else:
                    nums.append(r)
                    pre_2, pre_1 = pre_1, r
            elif l <= pre_2:
                continue
            else:
                nums.append(r)
                pre_2, pre_1 = pre_1, r
        return len(nums)    # 错误



class Solution:
    # 分类讨论
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[1])
        pre_2, pre_1 = -1, -1
        for l, r in intervals:
            if l > pre_1:
                if l != r:
                    ans += 2     
                    pre_2, pre_1 = r - 1, r
                else:
                    ans += 1
                    pre_2, pre_1 = pre_1, r
            elif l <= pre_2:
                continue
            else:
                ans += 1
                if r == pre_1:
                    pre_2 = r - 1
                else:
                    pre_2, pre_1 = pre_1, r
        return ans


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[1])
        pre = [-1, -1]
        for l, r in intervals:
            if l > pre[-1]:
                if l != r:
                    ans += 2
                    pre[0], pre[1] = r - 1, r
                else:
                    ans += 1
                    pre[0], pre[1] = pre[1], r
            elif l <= pre[0]:
                continue
            else:
                ans += 1
                if r == pre[-1]:
                    pre[0] = r -1
                else:
                    pre[0], pre[1] = pre[1], r
        return ans


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 右端点从小到大，保证贪心处理边缘点的正确性，同时右端点一样的时候优先处理长度最短的区间，因为该区间可选点最少同时会覆盖其他区间
        intervals.sort(key=lambda x:(x[1], -x[0]))
        # 由于我们是单调递增添加元素，维护当前集合前二大的元素即可判断是否需要添加新的
        a, b, ans = -1, -1, 0
        for left, right in intervals:
            # 如果区间左端点也在当前最大元素的右边，说明需要从该区间添加两个新点(可以理解为递归，前面的不再起作用)
            if left > b:
                # 贪心取最大的两个点
                a, b, ans = right - 1, right, ans + 2
            # 如果区间左端点位于当前最大元素与次大元素的中间，说明最大元素本身是区间内的一个点了
            elif left > a:
                # 我们还需要再取一个，贪心取该区间最大，原来的b成为次大
                a, b, ans = b, right, ans + 1
        return ans
