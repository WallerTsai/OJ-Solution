import sys

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
        while left < right:
            if left & 1:
                sml = self.op(sml, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self.op(self.tree[right], smr)
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

def main():

    data = sys.stdin.read().strip().split()
    if not data: return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    li_a = [(int(next(it)), 1) for _ in range(n)]
    
    def op(a, b):
        return (a[0] + b[0], a[1] + b[1])
    
    e = (0, 0)
    
    def mapping(f, data):
        return (data[0] + f * data[1], data[1])
    
    def composition(new_f, old_f):
        return new_f + old_f
    
    id_lazy = 0
    
    st = LazySegmentTree(op, e, mapping, composition, id_lazy, li_a)
    
    res = []
    for _ in range(m):
        flag = next(it)
        if flag == '1':
            l = int(next(it))
            r = int(next(it))
            k = int(next(it))
            st.update(l - 1, r, k)
        else:
            l = int(next(it))
            r = int(next(it))
            s = st.query(l - 1, r)
            res.append(str(s[0]))
            
    sys.stdout.write('\n'.join(res))

if __name__ == '__main__':
    main()