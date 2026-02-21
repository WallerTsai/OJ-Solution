from math import gcd

pow2 = lambda x : pow(x, 2)

class Solution:
    # 先处理平方，然后两数之和
    def countTriples(self, n: int) -> int:
        ans = 0
        li = [pow2(x) for x in range(1, n + 1)]
        aset = set(li)
        for i in range(n):
            for j in range(i, n):
                if li[i] + li[j] > li[-1]:
                    break
                if li[i] + li[j] in aset:
                    ans += 1
        return ans * 2  # 67ms


class Solution:
    # 灵神
    # https://zhuanlan.zhihu.com/p/1978057341963368012
    def countTriples(self, n: int) -> int:
        ans = 0
        u = 3
        while pow2(u) <= 2 * n:
            v = 1
            while v < u and pow2(u) + pow2(v) <= 2 * n:
                if gcd(u, v) == 1:
                    ans += 2 * n // (pow2(u) + pow2(v))
                v += 2
            u += 2
        return ans * 2  # 0ms
    



class Solution:
    # f佬
    def countTriples(self, n: int) -> int:
        import numpy as np

        # 生成从1到n-1的整数的平方数组
        a = np.square(np.arange(1, n, dtype=int))
        b = a.copy()
        
        # 使用广播机制计算a和b中所有可能的平方和
        # a[:, None]将a转换为列向量，b[None, :]将b转换为行向量
        # 然后逐元素相加，得到一个二维数组c
        c = a[:, None] + b[None, :]
        print(c.shape)
        
        # 筛选出c中小于等于n^2的元素，形成一个一维数组
        c = c[c <= n * n]
        # 对筛选后的数组c中的每个元素取平方根，并将结果转换为整数类型
        rt = np.sqrt(c).astype(int)
        
        # 计算rt的平方是否等于c，得到一个布尔数组
        # 使用np.sum统计布尔数组中True的数量，即满足条件的三元组数量
        # 使用.item()将结果从NumPy数组转换为Python原生整数类型并返回
        return np.sum(np.square(rt) == c).item()    # 68ms