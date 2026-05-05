from collections import defaultdict
from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        g = defaultdict(set)
        for i in range(n):
            # 主对角线元素不能为0
            if lcp[i][i] == 0:
                return ""
            # 长度问题
            if lcp[i][i] > n - i:
                return ""
            for j in range(i + 1, n):
                t = lcp[i][j]
                # 长度问题
                if t > n - j:
                    return ""
                # 主对角线不对称
                if lcp[j][i] != t:
                    return ""
                a, b = i, j
                for _ in range(t):
                    g[a].add(b)
                    g[b].add(a)
                    a += 1
                    b += 1

        start = ord('a')
        ans = [None] * n
        for i in range(n):
            if ans[i] is not None:
                continue
            st = [i]
            ans[i] = start
            while st:
                idx = st.pop()
                for j in g[idx]:
                    if ans[j] is None:
                        ans[j] = start
                        st.append(j)
            start += 1
        
        return ''.join(map(chr, ans)) if all(ans) else ""   # 错误


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        g = defaultdict(set)
        for i in range(n):
            # 主对角线元素不能为0
            if lcp[i][i] == 0:
                return ""
            # 长度问题
            if lcp[i][i] > n - i:
                return ""
            for j in range(i + 1, n):
                t = lcp[i][j]
                # 长度问题
                if t > n - j:
                    return ""
                # 主对角线不对称
                if lcp[j][i] != t:
                    return ""
                a, b = i, j
                for _ in range(t):
                    g[a].add(b)
                    g[b].add(a)
                    a += 1
                    b += 1

        start = ord('a')
        ans = [None] * n
        for i in range(n):
            if ans[i] is not None:
                continue
            st = [i]
            ans[i] = start
            while st:
                idx = st.pop()
                for j in g[idx]:
                    if ans[j] is None:
                        ans[j] = start
                        st.append(j)
            start += 1
        if start > ord('z') + 1:
            return ""
        ans_lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if ans[i] == ans[j]:
                    ans_lcp[i][j] = ans_lcp[i + 1][j + 1] + 1
                if ans_lcp[i][j] != lcp[i][j]:
                    return ""
        
        return ''.join(map(chr, ans)) if all(ans) else ""   # 超时
    

class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        ans = [''] * n
        c = ord('a')
        
        # 贪心构造字符串
        for i in range(n):
            if ans[i] == '':
                if c > ord('z'):
                    return ""
                ans[i] = chr(c)
                c += 1
            
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    ans[j] = ans[i]
                    
        word = "".join(ans)
        
        # 原地校验 LCP 矩阵是否合法
        for i in range(n):
            for j in range(n):
                if word[i] == word[j]:
                    # 如果字符相同，期望的 LCP 值应该是右下角的值 + 1
                    expected = lcp[i + 1][j + 1] + 1 if i + 1 < n and j + 1 < n else 1
                    if lcp[i][j] != expected:
                        return ""
                else:
                    # 如果字符不同，LCP 值必须为 0
                    if lcp[i][j] != 0:
                        return ""
                        
        return word
    


# 并查集
# 自用第三版并查集
class UnionFind:
    def __init__(self, n: int, base: int = 0):
        """
        base = 0: 节点编号 0 ~ n - 1
        bsee = 1: 节点编号 1 ~ n 
        """
        _size = n + 1 if base == 1 else n
        self.parent = list(range(_size))
        self.rank = [0] * _size         # 秩, 按秩合并，控制树高
        self.block_size = [1] * _size   # 每个连通块的节点数量
        self.block_count = n                  # 连通块数量

    def find(self, x: int) -> int:
        """ 迭代路径压缩 """
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[x] != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp

        return root

    def union(self, x: int, y: int) -> bool:
        """ 按秩合并 """
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.block_size[root_x] += self.block_size[root_y]
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.block_count -= 1

        return True
    
    def merge(self, _from: int, _to: int) -> bool:
        """ 有向合并 """
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        
        self.parent[x] = y
        self.block_size[y] += self.block_size[x]
        if self.rank[x] >= self.rank[y]:
            self.rank[y] = self.rank[x] + 1
        self.block_count -= 1

        return True
    
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def get_block_size(self, x: int) -> int:
        """返回 x 所在连通块的节点数"""
        return self.block_size[self.find(x)]
    
    def get_block_count(self) -> int:
        """返回当前连通块总数"""
        return self.block_count

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        uf = UnionFind(n)

        for i in range(n):
            # 主对角线元素不能为0
            if lcp[i][i] == 0:
                return ""
            # 长度问题
            if lcp[i][i] > n - i:
                return ""
            for j in range(i + 1, n):
                t = lcp[i][j]
                if t == 0:
                    continue
                # 长度问题
                if t > n - j:
                    return ""
                # 主对角线不对称
                if lcp[j][i] != t:
                    return ""
                
                uf.union(i, j)

        # 构造答案
        ans = [""] * n
        _map = {}
        c = ord("a")
        for i in range(n):
            root = uf.find(i)
            if root not in _map:
                if c > ord('z'):
                    return ""
                _map[root] = chr(c)
                c += 1
            ans[i] = _map[root]

        # 原地校验
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if ans[i] == ans[j]:
                    t = lcp[i + 1][j + 1] + 1 if i + 1 < n and j + 1 < n else 1
                    if t != lcp[i][j]:
                        return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
        
        return ''.join(ans)