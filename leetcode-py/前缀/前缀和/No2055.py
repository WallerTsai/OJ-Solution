from math import inf
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pre_sum = [0] * n

        start_idx = 0
        while s[start_idx] != '|':
            start_idx += 1

        cur = pre = 0
        for i in range(start_idx,n):
            if s[i] == '|':
                pre += cur
                pre_sum[i] = pre
                cur = 0
            else:
                cur += 1
                pre_sum[i] = pre

        ans = []
        for i, j in queries:
            ans.append(pre_sum[j] - pre_sum[i])

        return ans  # 错误

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # presum: 统计*的前缀和, lefts: 统计每个坐标左边最近的|的坐标, rights: 统计每个坐标右边最近的|的坐标
        presum, lefts, rights, l = [0] * (n + 1), [-1] * n, [-1] * n, -1
        for i, c in enumerate(s):
            if c == '*':
                # 当前字符为*，前缀和个数加一
                presum[i + 1] = presum[i] + 1
            else:
                # 当前字符为|，前缀和个数不变
                presum[i + 1] = presum[i]
                # 更新最新的坐标最近坐标（接下来下次更新前最近的都是i）
                l = i
            lefts[i] = l
        # 右边与左边的更新同理，只需要从右往左
        r = -1
        for i, c in enumerate(s[::-1]):
            if c == '|':
                r = n - 1 - i
            rights[n - 1 - i] = r
        # 最终答案只有 左查询点的右边有蜡烛、右查询点的左边有蜡烛、且右边的蜡烛在左边的蜡烛右边中间才可能有*，否则肯定是0个
        return [presum[lefts[r]] - presum[rights[l]] if rights[l] >= 0 and lefts[r] >= 0 and rights[l] < lefts[r] else 0 for l, r in queries]