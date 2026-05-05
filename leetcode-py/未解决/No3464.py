from bisect import bisect_left
from typing import List

# 以下答案均来自灵神

class Solution:
    # 二分答案 + 二分查找
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 拉直
        li = []
        for x, y in points:
            if x == 0:
                li.append(y)
            elif y == side:
                li.append(side + x)
            elif x == side:
                li.append(side * 3 - y)
            else:
                li.append(side * 4 - x)
        li.sort()

        def check(low: int) -> bool:
            for start in li:
                cur = start
                end = start + side * 4 - low
                for _ in range(k - 1):
                    j = bisect_left(li, cur + low)
                    if j == len(li) or li[j] > end:
                        break
                    cur = li[j]
                else:
                    return True
                
            return False

        left = 1
        right = side * 4 // k + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1
    


class Solution:
    # 二分答案 + 倍增
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 拉直
        li = []
        for x, y in points:
            if x == 0:
                li.append(y)
            elif y == side:
                li.append(side + x)
            elif x == side:
                li.append(side * 3 - y)
            else:
                li.append(side * 4 - x)
        li.sort()

        n = len(li)
        k -= 1
        mx = k.bit_length()
        nxt = [[n] * mx for _ in range(n + 1)]
        def check(low: int) -> bool:
            # 预处理倍增数组 nxt
            j = n
            for i in range(n - 1, -1, -1):  # 转移来源在右边，要倒序计算
                while li[j - 1] >= li[i] + low:
                    j -= 1
                nxt[i][0] = j
                for l in range(1, mx):
                    nxt[i][l] = nxt[nxt[i][l - 1]][l - 1]
    
            # 枚举起点
            for i, start in enumerate(li):
                # 往后跳 k-1 步（注意上面把 k 减一了）
                cur = i
                for j in range(mx - 1, -1, -1):
                    if k >> j & 1:
                        cur = nxt[cur][j]
                if cur == n:  # 出界
                    break
                if a[cur] - start <= side * 4 - low:
                    return True
            return False

        left = 1
        right = side * 4 // k + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1
