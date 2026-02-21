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
    



    