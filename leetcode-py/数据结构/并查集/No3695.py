from collections import defaultdict
from typing import List




class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        aset = set()
        for a, b in swaps:
            aset.add(a)
            aset.add(b)

        n = len(nums)
        even = (n + 1) // 2

        li = []
        ans = 0

        for i, num in enumerate(nums):
            if i in aset:
                li.append(num)
                continue

            if i % 2:
                ans -= num
            else:
                ans += num
                even -= 1

        li.sort(reverse=True)
        ans += sum(li[:even])
        ans -= sum(li[even:])

        return ans  # 错误
    


class UnionFind:

    def __init__(self, n: int):
        self.parent =  list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        return True
    


from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))    # 有时候是 n - 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        return True

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        uf = UnionFind(n)
        
        for a, b in swaps:
            uf.merge(a, b)
        
        comp_indxe_dict = {}
        for i in range(n):
            root = uf.find(i)
            if root not in comp_indxe_dict:
                comp_indxe_dict[root] = []
            comp_indxe_dict[root].append(i)
        
        sum_even = 0
        sum_odd = 0
        
        for indices in comp_indxe_dict.values():
            even_count = sum(1 for idx in indices if idx % 2 == 0)
            
            numbers = [nums[i] for i in indices]
            numbers.sort(reverse=True)

            sum_even += sum(numbers[:even_count])
            sum_odd += sum(numbers[even_count:])
        
        return sum_even - sum_odd
    


# 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.odd = [i % 2 for i in range(n)]  # 集合中的奇数个数
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        fa = self._fa
        if fa[x] != x:
            fa[x] = self.find(fa[x])  # fa 改成代表元
        return fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合
        self.odd[y] += self.odd[x]  # 更新集合中的奇数个数

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        uf = UnionFind(len(nums))
        for p, q in swaps:
            uf.merge(p, q)

        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[uf.find(i)].append(x)  # 相同集合的元素分到同一组

        ans = 0
        for i, a in g.items():
            a.sort()
            odd = uf.odd[i]
            # 小的取负号，大的取正号
            for j, x in enumerate(a):
                ans += -x if j < odd else x
        return ans