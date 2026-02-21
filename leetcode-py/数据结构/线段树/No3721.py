import sys
from math import inf
from typing import List


# gemini 优化
import sys

# 针对 Python 递归深度做一下防御，虽然线段树主要是迭代
sys.setrecursionlimit(200000)

class LazySegTree:
    # 1. 使用 __slots__ 极度优化内存和属性访问速度
    __slots__ = '_n', '_log', '_size', '_d', '_lz'

    def __init__(self, v):
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        
        # 初始化数据
        # 默认值为 (inf, -inf)，对应 min/max 的单位元
        self._d = [(10**15, -10**15)] * (2 * self._size)
        self._lz = [0] * self._size
        
        # 2. 使用切片赋值代替循环，Python中速度极快
        self._d[self._size : self._size + self._n] = v
        
        # 建树
        d = self._d
        for i in range(self._size - 1, 0, -1):
            # 硬编码 op: (min(l, r), max(l, r))
            l, r = d[2 * i], d[2 * i + 1]
            d[i] = (
                l[0] if l[0] < r[0] else r[0],
                l[1] if l[1] > r[1] else r[1]
            )

    # 硬编码 op, mapping, composition 以避免函数调用开销
    # op: (min_val, max_val)
    # mapping: (val + f, val + f)
    # composition: f + g
    
    def _update(self, k):
        d = self._d
        l, r = d[2 * k], d[2 * k + 1]
        d[k] = (
            l[0] if l[0] < r[0] else r[0],
            l[1] if l[1] > r[1] else r[1]
        )

    def _all_apply(self, k, f):
        d = self._d
        val = d[k]
        d[k] = (val[0] + f, val[1] + f)
        if k < self._size:
            self._lz[k] += f

    def _push(self, k):
        lz = self._lz
        f = lz[k]
        if f != 0: # 0 是 lazy 的单位元
            # 手动展开 _all_apply 减少调用
            d = self._d
            
            # Left child
            idx = 2 * k
            val = d[idx]
            d[idx] = (val[0] + f, val[1] + f)
            if idx < self._size:
                lz[idx] += f
            
            # Right child
            idx = 2 * k + 1
            val = d[idx]
            d[idx] = (val[0] + f, val[1] + f)
            if idx < self._size:
                lz[idx] += f
                
            lz[k] = 0

    def set(self, p, x):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def update_range(self, left, right, f):
        # 对应 update(left, right, val)
        if left > right: return # 兼容习惯，虽然 ACL 通常是 [left, right)
        
        # 注意：ACL 默认是 [left, right)，你的原代码是 [left, right] 闭区间
        # 这里为了匹配你的原逻辑，我把 right + 1
        right += 1 
        
        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        l2 = left
        r2 = right
        
        while left < right:
            if left & 1:
                self._all_apply(left, f)
                left += 1
            if right & 1:
                right -= 1
                self._all_apply(right, f)
            left >>= 1
            right >>= 1

        left = l2
        right = r2

        for i in range(1, self._log + 1):
            if ((left >> i) << i) != left:
                self._update(left >> i)
            if ((right >> i) << i) != right:
                self._update((right - 1) >> i)

    def find_first_idx(self, ps):
        """
        利用 max_right 寻找第一个满足条件 nd[0] <= ps <= nd[1] 的索引
        逻辑：max_right(0, g) 寻找最长的前缀，使得 g 成立。
        我们定义 g 为“不包含 ps”，那么 max_right 返回的就是“第一个包含 ps 的索引”。
        """
        left = 0
        left += self._size
        
        # 必须先 push 根路径
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm_min, sm_max = 10**15, -10**15 # Identity
        
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            
            # 模拟 op(sm, d[left])
            curr = self._d[left]
            next_min = sm_min if sm_min < curr[0] else curr[0]
            next_max = sm_max if sm_max > curr[1] else curr[1]
            
            # 判断条件：NOT (nd[0] <= ps <= nd[1])
            # 如果条件成立（即 ps 还没出现），继续向右
            if not (next_min <= ps <= next_max):
                sm_min = next_min
                sm_max = next_max
                left += 1
                continue
            
            # 如果条件不成立（即 ps 在当前区间内），钻取寻找第一个位置
            while left < self._size:
                self._push(left)
                left *= 2
                
                curr = self._d[left]
                check_min = sm_min if sm_min < curr[0] else curr[0]
                check_max = sm_max if sm_max > curr[1] else curr[1]
                
                # 如果左孩子不包含 ps，说明 ps 在右孩子，往右走
                if not (check_min <= ps <= check_max):
                    sm_min = check_min
                    sm_max = check_max
                    left += 1
            
            return left - self._size

        return self._n

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        # 预处理 evens 和 odds 的映射
        evens_set = set()
        odds_set = set()
        for x in nums:
            if x % 2 == 0:
                evens_set.add(x)
            else:
                odds_set.add(x)
        
        evens = {x: 2*i for i, x in enumerate(evens_set)}
        odds = {x: 2*i+1 for i, x in enumerate(odds_set)}
        
        if not evens or not odds: return 0
        
        # last 数组
        last = [-1] * (max(len(evens), len(odds)) * 2 + 2)
        
        # 初始化线段树数据
        # 对应原代码：[(0, 0)] + [(inf, -inf)] * len(nums)
        # 使用 10**15 作为 inf
        init_data = [(0, 0)] + [(10**15, -10**15)] * n
        seg = LazySegTree(init_data)
        
        ps = 0
        ans = 0
        
        for r, x in enumerate(nums):
            mapped_x = evens[x] if x % 2 == 0 else odds[x]
            p = last[mapped_x]
            
            if p != -1:
                # 区间更新 [p+1, r]
                # 注意：LazySegTree 的 update_range 已改为闭区间适应原逻辑
                val = -1 if x % 2 == 0 else 1
                seg.update_range(p + 1, r, val)
            else:
                ps += 1 if x % 2 == 0 else -1
            
            # 查询
            # 寻找第一个范围包含 ps 的索引
            l = seg.find_first_idx(ps)
            
            if l <= r:
                ans = max(ans, r - l + 1)
            
            # 单点修改
            seg.set(r + 1, (ps, ps))
            last[mapped_x] = r
            
        return ans



import sys
from typing import List

# 增加递归深度，防止深层递归爆栈
sys.setrecursionlimit(200000)

class LazySegTree:
    __slots__ = (
        '_n', '_log', '_size', 
        '_d', '_lz', 
        '_op', '_e', '_mapping', '_composition', '_id'
    )

    def __init__(self, op, e, mapping, composition, id_, v):
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            self._n = v
            self._log = (self._n - 1).bit_length()
            self._size = 1 << self._log
            self._d = [e] * (2 * self._size)
            self._lz = [id_] * self._size
        else:
            self._n = len(v)
            self._log = (self._n - 1).bit_length()
            self._size = 1 << self._log
            self._d = [e] * (2 * self._size)
            self._lz = [id_] * self._size
            # 2. 使用切片赋值代替循环，速度提升显著
            self._d[self._size : self._size + self._n] = v
            
            # 初始化 update
            # 局部变量加速
            op_func = self._op
            d = self._d
            for i in range(self._size - 1, 0, -1):
                d[i] = op_func(d[2 * i], d[2 * i + 1])

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k, f):
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k):
        # 3. 这里的判断非常频繁，使用局部变量优化
        lz_val = self._lz[k]
        if lz_val == self._id:
            return
        
        # 缓存成员变量
        d = self._d
        lz = self._lz
        mapping = self._mapping
        composition = self._composition
        size = self._size
        
        # 左孩子
        idx = 2 * k
        d[idx] = mapping(lz_val, d[idx])
        if idx < size:
            lz[idx] = composition(lz_val, lz[idx])
        
        # 右孩子
        idx = 2 * k + 1
        d[idx] = mapping(lz_val, d[idx])
        if idx < size:
            lz[idx] = composition(lz_val, lz[idx])
        
        lz[k] = self._id

    def set(self, p, x):
        p += self._size

        push = self._push
        for i in range(self._log, 0, -1):
            push(p >> i)
        self._d[p] = x
        
        update = self._update
        for i in range(1, self._log + 1):
            update(p >> i)

    def get(self, p):
        p += self._size
        push = self._push
        for i in range(self._log, 0, -1):
            push(p >> i)
        return self._d[p]

    def prod(self, left, right):
        if left == right:
            return self._e

        left += self._size
        right += self._size

        push = self._push
        op = self._op
        d = self._d
        
        # Smart Push: 只 Push 必要的节点
        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                push(left >> i)
            if ((right >> i) << i) != right:
                push((right - 1) >> i)

        sml = self._e
        smr = self._e
        
        while left < right:
            if left & 1:
                sml = op(sml, d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(d[right], smr)
            left >>= 1
            right >>= 1

        return op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def apply(self, left, right=None, f=None):
        if f is None:
            # 模式 1: apply(p, f)
            p = left
            f_val = right
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f_val, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        
        else:
            # 模式 2: apply(left, right, f)
            if left == right:
                return

            left += self._size
            right += self._size
            
            push = self._push
            
            # Smart Push
            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    push(left >> i)
                if ((right >> i) << i) != right:
                    push((right - 1) >> i)

            l2 = left
            r2 = right
            
            d = self._d
            lz = self._lz
            mapping = self._mapping
            composition = self._composition
            size = self._size
            
            while left < right:
                if left & 1:
                    d[left] = mapping(f, d[left])
                    if left < size:
                        lz[left] = composition(f, lz[left])
                    left += 1
                if right & 1:
                    right -= 1
                    d[right] = mapping(f, d[right])
                    if right < size:
                        lz[right] = composition(f, lz[right])
                left >>= 1
                right >>= 1
            
            left = l2
            right = r2
            
            update = self._update
            # Smart Update
            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    update(left >> i)
                if ((right >> i) << i) != right:
                    update((right - 1) >> i)

    def max_right(self, left, g):
        if left == self._n:
            return self._n

        left += self._size
        push = self._push
        for i in range(self._log, 0, -1):
            push(left >> i)

        op = self._op
        d = self._d
        sm = self._e
        first = True
        
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(op(sm, d[left])):
                while left < self._size:
                    push(left)
                    left *= 2
                    if g(op(sm, d[left])):
                        sm = op(sm, d[left])
                        left += 1
                return left - self._size
            sm = op(sm, d[left])
            left += 1

        return self._n

    def min_left(self, right, g):
        if right == 0:
            return 0

        right += self._size
        push = self._push
        for i in range(self._log, 0, -1):
            push((right - 1) >> i)

        op = self._op
        d = self._d
        sm = self._e
        first = True
        
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(op(d[right], sm)):
                while right < self._size:
                    push(right)
                    right = 2 * right + 1
                    if g(op(d[right], sm)):
                        sm = op(d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = op(d[right], sm)

        return 0

# ==============================================================================
# Solution (外部实现，不修改模板)
# ==============================================================================

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. 定义线段树的操作逻辑
        # 我们需要同时维护区间最小值和最大值，以便使用 max_right 查找 0
        # 节点数据结构: (min_val, max_val)
        
        INF = 10**18
        
        def op(a, b):
            # 合并左右子树：取最小的 min，最大的 max
            return (min(a[0], b[0]), max(a[1], b[1]))
        
        e = (INF, -INF) # 幺元
        
        def mapping(f, a):
            # 区间加 f：min 和 max 都增加 f
            if a == e: return e # 避免幺元被更新
            return (a[0] + f, a[1] + f)
        
        def composition(f, g):
            # 懒标记叠加：f + g
            return f + g
        
        id_ = 0 # 懒标记单位元
        
        # 初始状态：所有位置的值为 0 => (0, 0)
        # 这里的含义是：初始时，任何 nums[l...-1] 的 distinct diff 都是 0
        init_data = [(0, 0) for _ in range(n)]
        
        seg = LazySegTree(op, e, mapping, composition, id_, init_data)
        
        last_pos = {}
        max_len = 0
        
        # 判定函数工厂：用于 max_right
        # 寻找第一个使得 min <= 0 的位置（当前是正数时）
        def check_pos(val_pair):
            return val_pair[0] > 0
            
        # 寻找第一个使得 max >= 0 的位置（当前是负数时）
        def check_neg(val_pair):
            return val_pair[1] < 0

        for r, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            last_pos[x] = r
            
            # 如果是奇数，区间 [prev+1, r] 的计数 +1
            # 如果是偶数，区间 [prev+1, r] 的计数 -1
            diff = 1 if x % 2 != 0 else -1
            
            # 更新线段树：注意这里是对下标范围 update
            # 表示对于所有 l ∈ [prev+1, r]，区间 nums[l...r] 的 diff 值增加了
            seg.apply(prev + 1, r + 1, diff)
            
            # 我们需要找到 [0, r+1) 范围内第一个值为 0 的下标 l
            # 利用值的连续性（相邻元素差 1）和 max_right
            
            start_val_pair = seg.get(0) # 获取位置 0 的当前值
            start_val = start_val_pair[0] # min 和 max 应该相等，取 min 即可
            
            found_idx = -1
            
            if start_val == 0:
                found_idx = 0
            elif start_val > 0:
                # 当前是正数，找第一个变非正数的位置（即 0，因为连续）
                # max_right 返回的是满足条件（>0）的最长前缀长度，即第一个 <=0 的下标
                idx = seg.max_right(0, check_pos)
                if idx <= r:
                    found_idx = idx
            else: # start_val < 0
                # 当前是负数，找第一个变非负数的位置（即 0，因为连续）
                # max_right 返回的是满足条件（<0）的最长前缀长度，即第一个 >=0 的下标
                idx = seg.max_right(0, check_neg)
                if idx <= r:
                    found_idx = idx
            
            if found_idx != -1:
                # 再次确认找到的值确实是 0 (理论上必然是，除非逻辑有误或越界)
                # 这一步在提交时可以注释掉以优化性能
                # assert seg.get(found_idx)[0] == 0
                max_len = max(max_len, r - found_idx + 1)
                
        return max_len
    


import sys
from typing import List

# =================================================================
# 优化版 LazySegTree 模板 (直接粘贴即可)
# =================================================================
class LazySegTree:
    __slots__ = ('_op', '_e', '_mapping', '_composition', '_id', 
                 '_n', '_log', '_size', '_d', '_lz')

    def __init__(self, op, e, mapping, composition, id_, v):
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v
        
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        
        d = self._d
        size = self._size
        for i in range(self._n):
            d[size + i] = v[i]
        
        op_func = self._op 
        for i in range(size - 1, 0, -1):
            d[i] = op_func(d[2 * i], d[2 * i + 1])

    def _update(self, k):
        d = self._d
        d[k] = self._op(d[2 * k], d[2 * k + 1])

    def _all_apply(self, k, f):
        d = self._d
        d[k] = self._mapping(f, d[k])
        if k < self._size:
            lz = self._lz
            lz[k] = self._composition(f, lz[k])

    def _push(self, k):
        lz = self._lz
        f = lz[k]
        if f != self._id:
            self._all_apply(2 * k, f)
            self._all_apply(2 * k + 1, f)
            lz[k] = self._id

    def set(self, p, x):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left, right):
        if left == right:
            return self._e
        left += self._size
        right += self._size
        log = self._log
        for i in range(log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e
        smr = self._e
        op = self._op
        d = self._d
        while left < right:
            if left & 1:
                sml = op(sml, d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(d[right], smr)
            left >>= 1
            right >>= 1
        return op(sml, smr)

    def apply(self, left, right=None, f=None):
        if right is None:
            p = left
            f_val = left if f is None else f
            if f is None: f = right
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            if left == right: return
            left += self._size
            right += self._size
            log = self._log
            for i in range(log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)
            l2, r2 = left, right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left, right = l2, r2
            for i in range(1, log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left, g):
        if left == self._n: return self._n
        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)
        sm = self._e
        first = True
        op = self._op
        d = self._d
        size = self._size
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0: left >>= 1
            if not g(op(sm, d[left])):
                while left < size:
                    self._push(left)
                    left *= 2
                    if g(op(sm, d[left])):
                        sm = op(sm, d[left])
                        left += 1
                return left - size
            sm = op(sm, d[left])
            left += 1
        return self._n

# =================================================================
# 题目解法 Solution
# =================================================================

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # 1. 预处理离散化映射
        # Evens -> 0, 2, 4...
        # Odds -> 1, 3, 5...
        evens_set = set(x for x in nums if x % 2 == 0)
        odds_set = set(x for x in nums if x % 2 == 1)
        
        # 优化: 使用字典推导式
        evens = {x: 2*i for i, x in enumerate(evens_set)}
        odds = {x: 2*i+1 for i, x in enumerate(odds_set)}
        
        if not evens or not odds: 
            return 0
            
        # 2. 定义线段树的操作函数
        INF = 10**9
        
        # Op: 合并两个节点 (min_val, max_val)
        # 注意：为了性能，这里使用简单的 if else 而不是 min/max 函数调用
        def op(a, b):
            return (a[0] if a[0] < b[0] else b[0], 
                    a[1] if a[1] > b[1] else b[1])
        
        e = (INF, -INF)
        
        # Mapping: Lazy标记(int) 作用于 数据(tuple)
        def mapping(f, a):
            return (a[0] + f, a[1] + f)
            
        # Composition: Lazy标记(int) 合并
        def composition(f, g):
            return f + g
            
        id_lazy = 0
        
        # 3. 初始化线段树
        # 初始状态: index 0 是 (0, 0)，其他是 (INF, -INF)
        # 数组总长度为 len(nums) + 1
        n = len(nums)
        init_data = [(0, 0)] + [e] * n
        
        seg = LazySegTree(op, e, mapping, composition, id_lazy, init_data)
        
        # 4. 主逻辑
        last = [-1] * (2 * (len(evens) + len(odds)) + 5) # 稍微开大一点避免越界
        ps = 0
        ans = 0
        
        for r, x in enumerate(nums):
            # 映射值
            mapped_x = evens[x] if x % 2 == 0 else odds[x]
            
            p = last[mapped_x]
            
            if p != -1:
                # 之前出现过，进行区间更新
                # 原代码: update(p+1, r, val) (闭区间)
                # 现代码: apply(p+1, r+1, val) (左闭右开)
                val = -1 if x % 2 == 0 else 1
                seg.apply(p + 1, r + 1, val)
            else:
                # 第一次出现，更新当前前缀和
                ps += 1 if x % 2 == 0 else -1
            
            # 查询
            # 原逻辑: find_right(0, lambda: min <= ps <= max)
            # 含义: 找到第一个满足 ps 在范围内的 index
            # 
            # max_right 逻辑: 找到第一个不满足 g 的 index
            # 所以 g 应该是: ps 不在范围内 (ps < min or ps > max)
            # 当 g 为 False 时 (即 ps 在范围内了)，max_right 停止并返回该 index
            l = seg.max_right(0, lambda nd: nd[0] > ps or nd[1] < ps)
            
            # 如果找到了有效的 l (l <= r)，更新答案
            # 注意: r 是当前 nums 的下标，对应 seg 中的下标是 r+1
            # 原代码计算长度是用 r - l + 1，这里的 r 是当前遍历到的索引
            if l <= r:
                ans = ans if ans > (r - l + 1) else (r - l + 1)
            
            # 单点更新当前位置 r+1
            seg.set(r + 1, (ps, ps))
            
            # 更新 last 记录
            last[mapped_x] = r
            
        return ans