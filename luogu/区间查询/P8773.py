import sys

data = sys.stdin.read().strip().split()
it = iter(data)

n = int(next(it))
m = int(next(it))
x = int(next(it))

li = [0] * (n + 1)
for i in range(1, n + 1):
    li[i] = int(next(it))

def func1():
    # 暴力
    pre = [0] * (n + 1)
    pos = dict()

    for i in range(1, n + 1):
        target = li[i] ^ x
        if target in pos:
            pre[i] = pos[target]
        pos[li[i]] = i

    res = []
    for _ in range(m):
        l = int(next(it))
        r = int(next(it))
        found = False
        for i in range(l, r + 1):
            if pre[i] >= l:
                found = True
                break

        res.append("yes" if found else "no")

    sys.stdout.write('\n'.join(res))


def func2():
    # 前缀最值
    max_idx = [0] * (n + 1)
    pos = dict()

    for i in range(1, n + 1):
        v = li[i]
        target = v ^ x
        max_idx[i] = max(pos.get(target, -1), max_idx[i - 1])
        pos[v] = i

    res = []
    for _ in range(m):
        l = int(next(it))
        r = int(next(it))

        res.append("yes" if max_idx[r] >= l else "no")

    sys.stdout.write('\n'.join(res))



class FenwickTreeMax:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, index: int, value: int) -> None:
        while index <= self.n:
            self.tree[index] = max(self.tree[index], value)
            index += self.lowbit(index)

    def query(self, index: int) -> int:
        res = 0
        while index > 0:
            res = max(res, self.tree[index])
            index -= self.lowbit(index)
        return res

def func3():
    # 树状数组
    t = FenwickTreeMax(n)
    pos = dict()

    for i in range(1, n + 1):
        v = li[i]
        target = v ^ x
        pre_idx = -1

        if target in pos:
            pre_idx = pos[target]
        pos[v] = i

        if pre_idx > 0:
            t.update(i, pre_idx)

    res = []
    for _ in range(m):
        l = int(next(it))
        r = int(next(it))

        pre_idx = t.query(r)
        res.append("yes" if pre_idx >= l else "no")

    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    func3()



# 下面是：gemini 给的线段树版本
import sys

# 必须增加递归深度，否则线段树建树或查询时会爆栈
sys.setrecursionlimit(300000)

# --- 线段树模板 (维护区间最大值) ---
class SegmentTreeMax:
    def __init__(self, data, n):
        self.n = n
        self.data = data  # 这里的 data 就是 pre 数组
        # 线段树数组大小一般开 4n
        self.tree = [0] * (4 * n)
        # 初始化建树
        self._build(1, 1, n)

    # 内部建树函数
    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            self._build(2 * node, start, mid)
            self._build(2 * node + 1, mid + 1, end)
            # 核心：父节点存储子节点的最大值
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    # 区间查询函数 [l, r]
    def query(self, l, r):
        return self._query(1, 1, self.n, l, r)

    def _query(self, node, start, end, l, r):
        # 1. 区间不相交
        if r < start or end < l:
            return 0  # 返回 0 因为 0 不会影响 max 比较
        
        # 2. 当前节点区间完全被查询区间包含
        if l <= start and end <= r:
            return self.tree[node]
            
        # 3. 递归查询子区间
        mid = (start + end) // 2
        val_left = self._query(2 * node, start, mid, l, r)
        val_right = self._query(2 * node + 1, mid + 1, end, l, r)
        
        return max(val_left, val_right)

# --- 主逻辑 ---
def main():
    # 快速读入
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
        x = int(next(iterator))

        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(next(iterator))

        # --- 预处理 pre 数组 ---
        # pre[i] 表示 a[i] 左侧最近的配对数的下标
        pos = {}  # 使用 dict 记录位置
        pre = [0] * (n + 1)

        for i in range(1, n + 1):
            target = a[i] ^ x
            if target in pos:
                pre[i] = pos[target]
            pos[a[i]] = i

        # --- 套用线段树模板 ---
        # 传入计算好的 pre 数组进行建树
        st = SegmentTreeMax(pre, n)

        results = []
        for _ in range(m):
            l = int(next(iterator))
            r = int(next(iterator))

            # --- 核心判断 ---
            # 查询区间 [l, r] 内 pre 的最大值
            # 解释：如果在 [l, r] 之间存在一个数 a[i]，它的配对数在 pre[i]
            # 且 pre[i] >= l，说明这个配对数也在区间 [l, r] 内。
            max_pre = st.query(l, r)

            if max_pre >= l:
                results.append("yes")
            else:
                results.append("no")

        sys.stdout.write('\n'.join(results) + '\n')

    except StopIteration:
        pass

if __name__ == "__main__":
    main()