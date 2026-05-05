from math import gcd


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

class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        n = len(nums)
        cnt_p = 0

        op = gcd
        e = 0
        v = []
        for x in nums:
            if x % p == 0:
                x //= p
                cnt_p += 1
            else:
                x = 0
            v.append(x)

        st = SegmentTree(op, e, v)

        def check():
            g = st.all()
            if g != 1:
                return False
            if cnt_p < n:
                return True
            for i in range(n):
                left = st.query(0, i)
                right = st.query(i + 1, n)
                if gcd(left, right) == 1:
                    return True
            
            return False
        
        ans = 0
        for idx, val in queries:
            old = nums[idx]
            if old % p == 0:
                cnt_p -= 1
            
            nums[idx] = val
            st.set(idx, val // p if val % p == 0 else 0)
            if val % p == 0:
                cnt_p += 1

            if check():
                ans += 1
        return ans

