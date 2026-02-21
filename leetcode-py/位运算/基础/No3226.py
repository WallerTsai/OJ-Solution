class Solution:
    def minChanges(self, n: int, k: int) -> int:
    # 如果 n 和 k 的交集是 k , 那么 k 就是 n 的子集
        if n & k != k:
            return -1
        # 按位异
        res = (n ^ k).bit_count()
        return res
    

class Solution:
    def minChanges(self, n: int, k: int) -> int:
    # 如果 n 和 k 的并集是 n , 那么 k 就是 n 的子集
        if n | k != n:
            return -1
        # 按位异
        res = (n ^ k).bit_count()
        return res
    
class Solution:
# 作者：灵茶山艾府
# 如果 k 去掉 n 中所有元素后，变成了空集，那么 k 就是 n 的子集
    def minChanges(self, n: int, k: int) -> int:
        return -1 if k & ~n else (n ^ k).bit_count()

