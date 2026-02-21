# 自用模板
from typing import List


class LazySegmentTree:
    __slots__ = ('op', 'e', 'mapping', 'composition', 'id', 
                 'n', 'height', 'size', 'tree', 'lazy')

    def __init__(self, op, e, mapping, composition, id_, v):
        """
        op: (data, data) -> data
        e: data (单位元)
        mapping: (lazy, data) -> data
        composition: (new_lazy, old_lazy) -> new_lazy
        id_: lazy (单位元)
        v: 初始数组 (List[data]) 或 长度 (int)
        """
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id_

        if isinstance(v, int): v = [e] * v
        
        self.n = len(v)
        self.height = (self.n - 1).bit_length()
        self.size = 1 << self.height
        self.tree = [e] * (2 * self.size)
        self.lazy = [self.id] * self.size
        tree = self.tree
        size = self.size
        for i in range(self.n): tree[size + i] = v[i]
        for i in range(size - 1, 0, -1): self._pushup(i)

    def _pushup(self, k):
        """ 使用子节点更新父节点 k """
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def _apply_lazy(self, k, f):
        """ 将 lazy 标记 f 应用到节点 k """
        self.tree[k] = self.mapping(f, self.tree[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _pushdown(self, k):
        """ 下传节点 k 的 lazy 标记 """
        f = self.lazy[k]
        if f != self.id:
            self._apply_lazy(2 * k, f)
            self._apply_lazy(2 * k + 1, f)
            self.lazy[k] = self.id

    def query(self, left, right):
        """ 查询 [left, right) """
        if left == right: return self.e
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if ((left >> i) << i) != left: self._pushdown(left >> i)
            if ((right >> i) << i) != right: self._pushdown((right - 1) >> i)
        sml, smr = self.e, self.e
        op, tree = self.op, self.tree
        while left < right:
            if left & 1:
                sml = op(sml, tree[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(tree[right], smr)
            left >>= 1
            right >>= 1
        return self.op(sml, smr)

    def update(self, left, right, f):
        """ 区间 [left, right) 更新为 f """
        if left == right: return
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if ((left >> i) << i) != left: self._pushdown(left >> i)
            if ((right >> i) << i) != right: self._pushdown((right - 1) >> i)
        l2, r2 = left, right
        while left < right:
            if left & 1:
                self._apply_lazy(left, f)
                left += 1
            if right & 1:
                right -= 1
                self._apply_lazy(right, f)
            left >>= 1
            right >>= 1
        left, right = l2, r2
        for i in range(1, self.height + 1):
            if ((left >> i) << i) != left: self._pushup(left >> i)
            if ((right >> i) << i) != right: self._pushup((right - 1) >> i)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        # (max_lenght, left_lenght, left_char, right_lenght, right_char, size)
        # def make_data(ch): return (1, 1, ch, 1, ch, 1)
        v = [(1, 1, ch, 1, ch, 1) for ch in s]

        def op(left, right):
            if left[5] == 0:
                return right
            if right[5] == 0:
                return left
            
            cur_max = left[0] if left[0] > right[0] else right[0]

            if left[4] == right[2]:    # 中间字符一样
                comb_len = left[3] + right[1]
                if comb_len > cur_max:
                    cur_max = comb_len

            new_left_len = left[1]
            if left[1] == left[5] and left[4] == right[2]:
                new_left_len = left[5] + right[1]

            new_right_len = right[3]
            if right[3] == right[5] and left[4] == right[2]:
                new_right_len = right[5] + left[3]

            return (cur_max, new_left_len, left[2], new_right_len, right[4], left[5] + right[5])

        e = (0, 0, '#', 0, '#', 0)
        mapping = lambda f, data: f
        composition = lambda f, g: f
        id_lazy = None

        st = LazySegmentTree(op, e, mapping, composition, id_lazy, v)

        res = []
        for idx, ch in zip(queryIndices, queryCharacters):
            st.update(idx, idx + 1, (1, 1, ch, 1, ch, 1))
            res.append(st.tree[1][0])

        return res



# 以下是Gemini答案
class LazySegmentTree:
    __slots__ = ('op', 'e', 'mapping', 'composition', 'id', 
                 'n', 'height', 'size', 'tree', 'lazy')

    def __init__(self, op, e, mapping, composition, id_, v):
        self.op, self.e, self.mapping, self.composition, self.id = op, e, mapping, composition, id_
        self.n = len(v)
        self.height = (self.n - 1).bit_length()
        self.size = 1 << self.height
        self.tree = [e] * (2 * self.size)
        self.lazy = [id_] * self.size
        for i in range(self.n): self.tree[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1): self._pushup(i)

    def _pushup(self, k):
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def _apply_lazy(self, k, f):
        self.tree[k] = self.mapping(f, self.tree[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _pushdown(self, k):
        f = self.lazy[k]
        if f != self.id:
            self._apply_lazy(2 * k, f)
            self._apply_lazy(2 * k + 1, f)
            self.lazy[k] = self.id

    def set(self, p, x):
        p += self.size
        for i in range(self.height, 0, -1): self._pushdown(p >> i)
        self.tree[p] = x
        for i in range(1, self.height + 1): self._pushup(p >> i)

    def all(self):
        return self.tree[1]


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # 1. 定义 Data 结构: (max_l, pre_l, pre_c, suf_l, suf_c, size)
        def make_data(char):
            return (1, 1, char, 1, char, 1)

        # 2. 定义 op (合并逻辑)
        def op(L, R):
            # 处理单位元情况
            if L[5] == 0: return R
            if R[5] == 0: return L
            
            # a. 基础继承左右子区间的最大值
            res_max = L[0] if L[0] > R[0] else R[0]
            
            # b. 中间字符相同，尝试合并跨界长度
            if L[4] == R[2]:
                combined = L[3] + R[1]
                if combined > res_max: res_max = combined
            
            # c. 维护新的 pre_l (左边界连续长度)
            res_pre = L[1]
            if L[1] == L[5] and L[4] == R[2]:
                res_pre = L[5] + R[1]
            
            # d. 维护新的 suf_l (右边界连续长度)
            res_suf = R[3]
            if R[3] == R[5] and R[2] == L[4]:
                res_suf = R[5] + L[3]
            
            return (res_max, res_pre, L[2], res_suf, R[4], L[5] + R[5])

        # 3. 线段树其他要素
        e = (0, 0, '', 0, '', 0)
        mapping = lambda f, data: data        # 单点修改不需要映射
        composition = lambda f, g: f          # 不需要标记合并
        id_lazy = None                        # 无标记

        # 4. 初始化
        init_v = [make_data(c) for c in s]
        st = LazySegmentTree(op, e, mapping, composition, id_lazy, init_v)
        
        # 5. 处理查询
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            
            # 执行单点修改
            st.set(idx, make_data(char))
            
            # 获取全局最大值 (根节点数据的第一个元素)
            ans.append(st.all()[0])
            
        return ans
    


# 线段树(无懒标记)

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
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s_ords = [ord(c) - 97 for c in s]
        
        # Data 结构: (max_len, pre_len, pre_char, suf_len, suf_char, size)
        # 初始化单个节点的构造函数
        def make_node(val):
            return (1, 1, val, 1, val, 1)
        
        init_data = [make_node(x) for x in s_ords]

        def op(L, R):
            if L[5] == 0: return R
            if R[5] == 0: return L
            
            cur_max = L[0] if L[0] > R[0] else R[0]
            
            l_suf_len, l_suf_char = L[3], L[4]
            r_pre_len, r_pre_char = R[1], R[2]
            
            if l_suf_char == r_pre_char:
                comb_len = l_suf_len + r_pre_len
                if comb_len > cur_max:
                    cur_max = comb_len
            
            new_pre_len = L[1]
            if L[1] == L[5] and l_suf_char == r_pre_char:
                new_pre_len = L[5] + r_pre_len
            
            new_suf_len = R[3]
            if R[3] == R[5] and r_pre_char == l_suf_char:
                new_suf_len = R[5] + l_suf_len
            
            return (cur_max, new_pre_len, L[2], new_suf_len, R[4], L[5] + R[5])

        e = (0, 0, -1, 0, -1, 0)
        
        st = SegmentTree(op, e, init_data)
        
        ans = []
        for idx, char in zip(queryIndices, queryCharacters):
            val = ord(char) - 97
            st.set(idx, make_node(val))
            ans.append(st.all()[0])
            
        return ans