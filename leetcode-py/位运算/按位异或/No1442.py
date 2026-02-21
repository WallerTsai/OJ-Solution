from collections import defaultdict
from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    # 前缀和 暴力 O(n ** 3)
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prexor = [0] + list(accumulate(arr, xor))
        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j, n + 1):
                    a = prexor[j - 1] ^ prexor[i - 1]
                    b = prexor[k] ^ prexor[j - 1]
                    ans += (a == b)
        return ans  # 2589ms


class Solution:
    # 利用 异或性质 a == b <=> a ^ b = 0  O(n ** 2)
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prexor = [0] + list(accumulate(arr, xor))
        ans = 0
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                if (prexor[i - 1] == prexor[k]):
                    ans += k - i
        return ans  # 7ms
    
class Solution:
    # 利用 异或性质 + 哈希表优化 + 优化掉前缀和
    # 利用数学 (k - i1) + (k - i2) + (k - i3) + (k - i4) = 4*k - (i1+i2+i3+i4)
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        cnt = defaultdict(int)
        total_val = defaultdict(int)
        cur_xor = 0
        for k in range(n):
            cur_xor ^= arr[k]
            ans += cnt[cur_xor] * k - total_val[cur_xor]

            # 注意下面的哈希键
            # 我们需要记录的是 i 前面一项的前缀和
            # 参照上种方法的 prexor[i - 1] == prexor[k]
            cnt[cur_xor ^ arr[k]] += 1
            total_val[cur_xor ^ arr[k]] += k

        return ans # 3ms