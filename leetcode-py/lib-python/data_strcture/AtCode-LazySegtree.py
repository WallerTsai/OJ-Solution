# 参考 https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
class LazySegTree:
    def __init__(self, op, e, mapping, composition, id_, v):
        """
        op: 函子, 定义如何合并两个子节点的值 (data + data -> data)
        e: 变量, data 的单位元
        mapping: 函子, 定义 lazy 标记如何影响节点值 (lazy + data -> data)
        composition: 函子, 定义如何合并两个 lazy 标记 (new_lazy + old_lazy -> new_lazy)
        id_: 变量, lazy 的单位元
        v: 初始数组 (List) 或 长度 (int)
        """
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):  # 如果传入的是长度则生成一个单位元数组
            v = [e] * v
        
        self._n = len(v)
        self._log = (self._n - 1).bit_length()  # 树高
        self._size = 1 << self._log             # 大小
        
        self._d = [e] * (2 * self._size)    # 树
        self._lz = [self._id] * self._size  # 标记
        
        # 初始化数据
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        """ 更新操作 """
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k, f):
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:  # 非叶子节点 暂存标记
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k):
        """ 将节点 k 的lazy标记推给他的两个子节点, 并且清空自己 """
        # 只有当 lazy 标记不是单位元时才下传
        if self._lz[k] != self._id:
            self._all_apply(2 * k, self._lz[k])
            self._all_apply(2 * k + 1, self._lz[k])
            self._lz[k] = self._id

    def set(self, p, x):
        """ 单点修改 """
        p += self._size
        # 从根到叶子 push
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        # 从叶子到根 update
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        """ 单点查询 """
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left, right):
        """ 查询区间 [left, right) 的结果 """
        if left == right:
            return self._e

        left += self._size
        right += self._size

        # 将路径上的 lazy标记 推送下去(难理解)
        # left 处于某个父节点管辖范围的左边界则不推
        # right 处于某个父节点管辖范围的左边界则不推 
        # (right 取不到, 相当于 right - 1 处于其父节点的右边界)
        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e   # 左侧累计结果
        smr = self._e   # 右侧累计结果
        # (gemini 解释 因为_op操作可能不满足交换律，比如矩阵乘法，所以左右要分开存)
        
        while left < right:
            if left & 1:    # left 为右孩子
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:   # right 为右孩子(right - 1 为左孩子)
                right -= 1
                smr = self._op(self._d[right], smr)
            # 非以上情况, 可以只算他父节点的值
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def apply(self, left, right=None, f=None):
        """
        区间更新: apply(left, right, f) -> 更新 [left, right) 为 f
        单点更新: apply(p, f) -> 更新 p 为 f
        """
        if right is None: # 单点模式
            p = left
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else: # 区间模式
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            # (难理解)
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

            # 由下往上更新
            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left, g):
        """
        寻找区间 [left, x) 满足条件 g 的最大的 x。
        g: 函数, 接受一个 data, 返回 bool
        """

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            # (left & -left) != left 
            # 如果 left 是 2 的幂（比如 16, 8, 4），
            # 说明 left 节点覆盖了剩余的所有范围（一直到树的右边界）
            first = False
            while left % 2 == 0:    # 左孩子
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right, g):
        """
        寻找区间 [x, right) 满足条件 g 的最小的 x。
        g: 函数, 接受一个 data, 返回 bool
        """

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0
    



import sys

# 建议在提交代码头部加上这个，虽然线段树是迭代写的，但某些递归场景可能需要
# sys.setrecursionlimit(200000)

class LazySegTree:
    # 【优化1】使用 __slots__ 限制类属性，减少内存占用并加速属性访问
    __slots__ = ('_op', '_e', '_mapping', '_composition', '_id', 
                 '_n', '_log', '_size', '_d', '_lz')

    def __init__(self, op, e, mapping, composition, id_, v):
        """
        op: (data, data) -> data
        e: data (单位元)
        mapping: (lazy, data) -> data
        composition: (new_lazy, old_lazy) -> new_lazy
        id_: lazy (单位元)
        v: 初始数组 (List[data]) 或 长度 (int)
        """
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            # 【优化2】安全初始化：避免 [e] * v 导致的浅拷贝引用问题
            # 如果 e 是不可变对象(int/str)，这样写没问题；如果是 list，必须用下面的写法
            v = [e] * v 
        
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        
        # 初始化数据数组和 lazy 数组
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        
        # 将初始值填入叶子节点
        d = self._d
        size = self._size
        for i in range(self._n):
            d[size + i] = v[i]
        
        # 建树：从下往上更新
        # 【优化3】本地变量缓存 op，避免循环中频繁访问 self._op
        op_func = self._op 
        for i in range(size - 1, 0, -1):
            d[i] = op_func(d[2 * i], d[2 * i + 1])

    def _update(self, k):
        """ 更新节点 k 的值 (用子节点推导父节点) """
        d = self._d
        d[k] = self._op(d[2 * k], d[2 * k + 1])

    def _all_apply(self, k, f):
        """ 将 lazy 标记 f 应用到节点 k """
        d = self._d
        d[k] = self._mapping(f, d[k])
        # 如果不是叶子节点，需要把标记存到 lazy 数组中
        if k < self._size:
            lz = self._lz
            lz[k] = self._composition(f, lz[k])

    def _push(self, k):
        """ 下传 lazy 标记 """
        lz = self._lz
        f = lz[k]
        # 只有当标记不是单位元时才下传
        if f != self._id:
            self._all_apply(2 * k, f)
            self._all_apply(2 * k + 1, f)
            lz[k] = self._id

    def set(self, p, x):
        """ 单点修改: a[p] = x """
        p += self._size
        # 从根到叶子 push
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        
        self._d[p] = x
        
        # 从叶子到根 update
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        """ 单点查询: a[p] """
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left, right):
        """ 区间查询: 查询 [left, right) 的聚合值 """
        if left == right:
            return self._e

        left += self._size
        right += self._size

        # 预先处理 lazy 标记下传
        log = self._log
        for i in range(log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e
        smr = self._e
        
        # 【优化4】核心循环内的变量缓存
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
        """
        区间/单点修改
        用法1: apply(p, f) -> 单点 p 修改为 f
        用法2: apply(l, r, f) -> 区间 [l, r) 修改为 f
        """
        # 为了兼容两种调用方式的逻辑判断
        if right is None:
            # 单点模式: apply(p, f) -> 此时 f 在参数 right 的位置上
            p = left
            if f is None:
                f = right
            
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            
            self._d[p] = self._mapping(f, self._d[p])
            
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            # 区间模式: apply(l, r, f)
            if left == right:
                return

            left += self._size
            right += self._size
            log = self._log

            for i in range(log, 0, -1):
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

            for i in range(1, log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left, g):
        """
        寻找区间 [left, x) 满足条件 g 的最大的 x
        """
        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        
        # 缓存变量
        op = self._op
        d = self._d
        size = self._size
        
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            
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

    def min_left(self, right, g):
        """
        寻找区间 [x, right) 满足条件 g 的最小的 x
        """
        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        
        # 【优化5】min_left 内部循环缓存
        op = self._op
        d = self._d
        size = self._size
        
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and (right % 2):
                right >>= 1
            
            if not g(op(d[right], sm)):
                while right < size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(op(d[right], sm)):
                        sm = op(d[right], sm)
                        right -= 1
                return right + 1 - size
            
            sm = op(d[right], sm)
        
        return 0