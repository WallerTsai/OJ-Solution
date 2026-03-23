import random
from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import cache
from typing import List

# 根据题目给出的条件，区间查询相当于找区间内的众数
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.di = defaultdict(list)
        for i, x in enumerate(arr):
            self.di[x].append(i)


    @cache
    def query(self, left: int, right: int, threshold: int) -> int:
        for x, li in self.di.items():
            if len(li) < threshold:
                continue
            if bisect_left(li, right + 1) - bisect_left(li, left) >= threshold:
                return x
        return -1




class MajorityChecker:
    # 随机化 + cache
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.di = defaultdict(list)
        for i, x in enumerate(arr):
            self.di[x].append(i)
        self.items = list(self.di.items())

    @cache
    def query(self, left: int, right: int, threshold: int) -> int:
        # 尝试 30 次随机采样，命中众数的概率极高
        for _ in range(30):
            idx = random.randint(left, right)
            x = self.arr[idx]
            li = self.di[x]
            if len(li) < threshold:
                continue
            
            if bisect_left(li, right + 1) - bisect_left(li, left) >= threshold:
                return x
        return -1



# 自用线段树模板
class SegmentTree:
    __slots__ = ('op', 'e', 'n', 'height', 'size', 'tree')

    def __init__(self, op, e, v):
        """
        op: (data, data) -> data
        e: data (单位元)
        v: 初始数组 (List[data]) 或 长度 (int)
        """
        self.op = op
        self.e = e

        if isinstance(v, int):
            v = [e] * v
        
        self.n = len(v)
        self.height = (self.n - 1).bit_length()
        self.size = 1 << self.height
        
        self.tree = [e] * (2 * self.size)
        
        # 初始化数据
        tree = self.tree
        size = self.size
        for i in range(self.n):
            tree[size + i] = v[i]
        
        # 建树 (自底向上)
        for i in range(size - 1, 0, -1):
            self._pushup(i)

    def _pushup(self, k):
        """ 使用子节点更新父节点 k """
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def set(self, p, x):
        """ 单点修改: a[p] = x """
        p += self.size
        self.tree[p] = x
        
        # 自底向上更新，无需 pushdown，速度飞快
        for i in range(1, self.height + 1):
            self._pushup(p >> i)

    def get(self, p):
        """ 单点查询: a[p] """
        return self.tree[p + self.size]

    def query(self, left, right):
        """ 区间查询 [left, right) """
        if left == right:
            return self.e

        left += self.size
        right += self.size

        sml = self.e
        smr = self.e
        op = self.op
        tree = self.tree
        
        # 核心查询逻辑：无 pushdown，纯循环
        while left < right:
            if left & 1:
                sml = op(sml, tree[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(tree[right], smr)
            left >>= 1
            right >>= 1

        return op(sml, smr)

    def all(self):
        """ 查询整棵树的聚合值 """
        return self.tree[1]

    def max_right(self, left, g):
        """ 寻找区间 [left, x) 满足条件 g 的最大的 x (无 pushdown 版) """
        if left == self.n:
            return self.n

        left += self.size
        sm = self.e
        first = True
        tree = self.tree
        op = self.op
        size = self.size
        
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            
            if not g(op(sm, tree[left])):
                while left < size:
                    left *= 2
                    if g(op(sm, tree[left])):
                        sm = op(sm, tree[left])
                        left += 1
                return left - size
            
            sm = op(sm, tree[left])
            left += 1

        return self.n

    def min_left(self, right, g):
        """ 寻找区间 [x, right) 满足条件 g 的最小的 x (无 pushdown 版) """
        if right == 0:
            return 0

        right += self.size
        sm = self.e
        first = True
        tree = self.tree
        op = self.op
        size = self.size
        
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and (right % 2):
                right >>= 1
            
            if not g(op(tree[right], sm)):
                while right < size:
                    right = 2 * right + 1
                    if g(op(tree[right], sm)):
                        sm = op(tree[right], sm)
                        right -= 1
                return right + 1 - size
            
            sm = op(tree[right], sm)
        
        return 0
    

def op(v1, v2):
    # 摩尔投票
    c1, cnt1 = v1
    c2, cnt2 = v2
    if c1 == c2:
        return (c1, cnt1 + cnt2)
    elif cnt1 > cnt2:
        return (c1, cnt1 - cnt2)
    else:
        return (c2, cnt2 - cnt1)
    
e = (0, 0)


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

        v = [(x, 1) for x in arr]

        self.st = SegmentTree(op = op, e = e, v = v)

    def query(self, left: int, right: int, threshold: int) -> int:
        c, cnt = self.st.query(left, right + 1)
        li = self.pos[c]
        cnt = bisect_right(li, right) - bisect_left(li, left)

        return c if cnt >= threshold else -1
        