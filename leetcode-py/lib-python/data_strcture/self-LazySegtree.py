from math import inf


class LazySegTreeSum:
    def __init__(self, data):
        self.n = len(data)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [0] * (2 * self.size)  
        self.lz = [0] * self.size       
        self.sz = [1] * (2 * self.size) 

        for i in range(self.n):
            self.d[self.size + i] = data[i]
        
        for i in range(self.size - 1, 0, -1):
            self.update(i)
            self.sz[i] = self.sz[2 * i] + self.sz[2 * i + 1]

    def update(self, k):
        self.d[k] = self.d[2 * k] + self.d[2 * k + 1]

    def all_apply(self, k, val):
        self.d[k] += val * self.sz[k]
        if k < self.size:
            self.lz[k] += val

    def push(self, k):
        if self.lz[k] != 0: 
            self.all_apply(2 * k, self.lz[k])
            self.all_apply(2 * k + 1, self.lz[k])
            self.lz[k] = 0

    def add(self, l, r, val):
        l += self.size
        r += self.size
        
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push((r - 1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1: self.all_apply(l, val); l += 1
            if r & 1: r -= 1; self.all_apply(r, val)
            l >>= 1; r >>= 1
            
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l: self.update(l >> i)
            if ((r >> i) << i) != r: self.update((r - 1) >> i)

    def query(self, l, r):
        l += self.size
        r += self.size
        
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push((r - 1) >> i)
            
        s = 0
        while l < r:
            if l & 1: s += self.d[l]; l += 1
            if r & 1: r -= 1; s += self.d[r]
            l >>= 1; r >>= 1
        return s
    

class LazySegTreeMax:
    def __init__(self, data):
        self.n = len(data)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [-inf] * (2 * self.size)
        self.lz = [0] * self.size
        
        for i in range(self.n):
            self.d[self.size + i] = data[i]
        
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def update(self, k):
        self.d[k] = max(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, val):
        self.d[k] += val
        if k < self.size:
            self.lz[k] += val

    def push(self, k):
        if self.lz[k] != 0:
            self.all_apply(2 * k, self.lz[k])
            self.all_apply(2 * k + 1, self.lz[k])
            self.lz[k] = 0

    def add(self, l, r, val):
        l += self.size
        r += self.size
        
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push((r - 1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1: self.all_apply(l, val); l += 1
            if r & 1: r -= 1; self.all_apply(r, val)
            l >>= 1; r >>= 1
            
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l: self.update(l >> i)
            if ((r >> i) << i) != r: self.update((r - 1) >> i)

    def query(self, l, r):
        l += self.size
        r += self.size
        
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.push(l >> i)
            if ((r >> i) << i) != r: self.push((r - 1) >> i)
            
        res = inf
        while l < r:
            if l & 1: res = max(res, self.d[l]); l += 1
            if r & 1: r -= 1; res = max(res, self.d[r])
            l >>= 1; r >>= 1
        return res
    

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

        if isinstance(v, int):
            v = [e] * v
        
        self.n = len(v)
        self.height = (self.n - 1).bit_length()
        self.size = 1 << self.height
        
        self.tree = [e] * (2 * self.size)
        self.lazy = [self.id] * self.size
        
        tree = self.tree
        size = self.size
        for i in range(self.n):
            tree[size + i] = v[i]
        
        for i in range(size - 1, 0, -1):
            self._pushup(i)

    def _pushup(self, k):
        """ 使用子节点更新父节点 k """
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def _apply_lazy(self, k, f):
        """ 将 lazy 标记 f 应用到节点 k (内部 modify) """
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

    def set(self, p, x):
        """ 单点赋值: a[p] = x """
        p += self.size
        for i in range(self.height, 0, -1):
            self._pushdown(p >> i)
        
        self.tree[p] = x
        
        for i in range(1, self.height + 1):
            self._pushup(p >> i)

    def get(self, p):
        """ 单点查询: a[p] """
        p += self.size
        for i in range(self.height, 0, -1):
            self._pushdown(p >> i)
        return self.tree[p]

    def query(self, left, right):
        """ 区间查询: 查询 [left, right) 的聚合值 """
        if left == right:
            return self.e

        left += self.size
        right += self.size

        for i in range(self.height, 0, -1):
            if ((left >> i) << i) != left:
                self._pushdown(left >> i)
            if ((right >> i) << i) != right:
                self._pushdown((right - 1) >> i)

        sml = self.e
        smr = self.e
        
        tree = self.tree
        op = self.op

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

    def update(self, left, right=None, f=None):
        """ 
        区间/单点修改
        用法1: update(left, right, f) -> 区间 [left, right) 更新为 f
        用法2: update(p, f) -> 单点 p 更新为 f (兼容旧版 apply 写法)
        """
        if right is None:
            p = left
            f = left if f is None else f
            if f is None: f = right # handle args mess if any
            
            p += self.size
            for i in range(self.height, 0, -1):
                self._pushdown(p >> i)
            
            self._apply_lazy(p, f)
            
            for i in range(1, self.height + 1):
                self._pushup(p >> i)
        else:
            if left == right:
                return

            left += self.size
            right += self.size
            
            for i in range(self.height, 0, -1):
                if ((left >> i) << i) != left:
                    self._pushdown(left >> i)
                if ((right >> i) << i) != right:
                    self._pushdown((right - 1) >> i)

            l2 = left
            r2 = right
            
            while left < right:
                if left & 1:
                    self._apply_lazy(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._apply_lazy(right, f)
                left >>= 1
                right >>= 1
            
            left = l2
            right = r2

            for i in range(1, self.height + 1):
                if ((left >> i) << i) != left:
                    self._pushup(left >> i)
                if ((right >> i) << i) != right:
                    self._pushup((right - 1) >> i)

    def getall(self):
        """ 获取当前数组的所有元素 """
        for i in range(1, self.size):
            self._pushdown(i)
        return self.tree[self.size : self.size + self.n]

    def find_right(self, left, g):
        """ 寻找区间 [left, x) 满足条件 g 的最大的 x """
        if left == self.n:
            return self.n

        left += self.size
        for i in range(self.height, 0, -1):
            self._pushdown(left >> i)

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
                    self._pushdown(left)
                    left *= 2
                    if g(op(sm, tree[left])):
                        sm = op(sm, tree[left])
                        left += 1
                return left - size
            
            sm = op(sm, tree[left])
            left += 1

        return self.n

    def find_left(self, right, g):
        """ 寻找区间 [x, right) 满足条件 g 的最小的 x """
        if right == 0:
            return 0

        right += self.size
        for i in range(self.height, 0, -1):
            self._pushdown((right - 1) >> i)

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
                    self._pushdown(right)
                    right = 2 * right + 1
                    if g(op(tree[right], sm)):
                        sm = op(tree[right], sm)
                        right -= 1
                return right + 1 - size
            
            sm = op(tree[right], sm)
        
        return 0


# 基本模板
# 自用模板
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
