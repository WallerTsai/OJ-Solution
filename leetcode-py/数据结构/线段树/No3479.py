from math import isqrt
from typing import List


class Solution:
    # 分块
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = isqrt(n)
        section = (n + m - 1) // m
        maxV = [0] * section

        for i in range(n):
            maxV[i // m] = max(maxV[i // m], baskets[i])

        ans = 0
        for fruit in fruits:
            choose = 0
            for sec in range(section):
                if maxV[sec] < fruit:
                    continue
                maxV[sec] = 0
                for i in range(m):
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and not choose:
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        maxV[sec] = max(maxV[sec], baskets[pos])
                break
            if not choose:
                ans += 1
        return ans  # 15701ms
    
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # 线段树大小取 2 * 2^{⌈log2 n⌉}
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        # 建树：把 data 放到叶子区间
        for i, v in enumerate(data):
            self.tree[size + i] = v
        # 自底向上维护每个父节点的 max
        for i in range(size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx, val):
        # 将位置 pos 叶子节点更新为 value
        pos = self.size + idx
        self.tree[pos] = val
        pos //= 2
        # 然后向上更新其祖先节点的最大值
        while pos:
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def find_first(self, val):
        if self.tree[1] < val:  # 根节点都不够大
            return -1
        # 从根节点开始找
        idx = 1
        while idx < self.size:  # 还没到叶子
            # 左子树的最大值
            if self.tree[2 * idx] >= val:
                idx = 2 * idx
            else:
                idx = 2 * idx + 1
        # idx 是叶子，映射回原数组下标
        return idx - self.size


class Solution:
    # 作者：wxyz
    # 链接：https://leetcode.cn/problems/fruits-into-baskets-iii/solutions/3743955/xian-duan-shu-po-su-di-tui-er-fen-he-bin-k6xy/
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        ans = 0

        for qty in fruits:
            i = tree.find_first(qty)
            if i == -1:  # 没找到
                ans += 1
            else:
                # 用过之后把这个篮子容量置为 -1 表示已使用
                tree.update(i, -1)

        return ans

