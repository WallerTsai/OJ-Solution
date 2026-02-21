from collections import Counter, defaultdict
from math import gcd, inf
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # y = kx + b
        cnt = defaultdict(lambda: defaultdict(int)) # 注意嵌套写法

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                if dy < 0:
                    dy, dx = -dy, -dx
                # k = dy / dx if dx else inf
                # 上面的先不采纳，为了避免除法，用(dy, dx) 表示斜率
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                # dy * x - dx * y  + dx * b = 0
                # c = dx * b
                c = dx * y1 - dy * x1 if dx else x1
                
                cnt[(dy, dx)][c] += 1

        ans = 0
        for v in cnt.values():
            pre_num = 0
            for x in v.values():
                ans += x * pre_num
                pre_num += x
        return ans  # 错误，问题出在 if dy < 0 那里


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # y = kx + b
        cnt = defaultdict(lambda: defaultdict(int)) # 注意嵌套写法

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                
                # k = dy / dx if dx else inf
                # 上面的先不采纳，为了避免除法，用(dy, dx) 表示斜率
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # 统一符号
                if dy < 0 or (dy == 0 and dx < 0):
                    dy, dx = -dy, -dx
                # dy * x - dx * y  + dx * b = 0
                # c = dx * b
                c = dx * y1 - dy * x1 if dx else x1
                
                cnt[(dy, dx)][c] += 1

        ans = 0
        for v in cnt.values():
            pre_num = 0
            for x in v.values():
                ans += x * pre_num
                pre_num += x
        return ans  # 注意， 平行四边形重复统计一遍
    
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # y = kx + b
        cnt = defaultdict(lambda: defaultdict(int)) # 注意嵌套写法
        cnt_parallelogram = defaultdict(lambda: defaultdict(int))
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                
                # 长度二次方
                l = pow(dy, 2) + pow(dx, 2)

                # k = dy / dx if dx else inf
                # 上面的先不采纳，为了避免除法，用(dy, dx) 表示斜率
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # 统一符号
                if dy < 0 or (dy == 0 and dx < 0):
                    dy, dx = -dy, -dx
                # dy * x - dx * y  + dx * b = 0
                # c = dx * b
                c = dx * y1 - dy * x1 if dx else x1
                
                
                cnt[(dy, dx)][c] += 1
                cnt_parallelogram[(dy, dx)][l] += 1

        ans = 0
        for v in cnt.values():
            pre_num = 0
            for x in v.values():
                ans += x * pre_num
                pre_num += x

        for v in cnt_parallelogram.values():
            pre_num = 0
            for x in v.values():
                ans -= x * pre_num
                pre_num += x
            
        return ans  # 错误，相同斜率下的长度线段可能在同一条直线下
        
        
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # y = kx + b
        cnt = defaultdict(lambda: defaultdict(int)) # 注意嵌套写法
        cnt_parallelogram = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                
                # 长度二次方
                l = pow(dy, 2) + pow(dx, 2)

                # k = dy / dx if dx else inf
                # 上面的先不采纳，为了避免除法，用(dy, dx) 表示斜率
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # 统一符号
                if dy < 0 or (dy == 0 and dx < 0):
                    dy, dx = -dy, -dx
                # dy * x - dx * y  + dx * b = 0
                # c = dx * b
                c = dx * y1 - dy * x1 if dx else x1
                
                
                cnt[(dy, dx)][c] += 1
                cnt_parallelogram[l][(dy, dx)][c] += 1

        ans = 0
        for v in cnt.values():
            pre_num = 0
            for x in v.values():
                ans += x * pre_num
                pre_num += x

        num_parallelogram = 0
        for l in cnt_parallelogram.values():
            for k in l.values():
                pre_num = 0
                for x in k.values():
                    num_parallelogram += x * pre_num
                    pre_num += x

        return ans - num_parallelogram // 2 # 3549ms


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # ax + yb + c = 0
        cnt = defaultdict(lambda: defaultdict(int)) # 注意嵌套写法
        cnt_parallelogram = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y1 - y2
                dx = x1 - x2
                
                # 长度二次方
                l = pow(dy, 2) + pow(dx, 2)

                # k = dy / dx if dx else inf
                # 上面的先不采纳，为了避免除法，用(dy, dx) 表示斜率
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # 统一符号
                if dy < 0 or (dy == 0 and dx < 0):
                    dy, dx = -dy, -dx
                # dy * x - dx * y  + dx * b = 0
                # c = dx * b
                c = dx * y1 - dy * x1
                
                
                cnt[(dy, dx)][c] += 1
                cnt_parallelogram[l][(dy, dx)][c] += 1

        ans = 0
        for v in cnt.values():
            pre_num = 0
            for x in v.values():
                ans += x * pre_num
                pre_num += x

        num_parallelogram = 0
        for l in cnt_parallelogram.values():
            for k in l.values():
                pre_num = 0
                for x in k.values():
                    num_parallelogram += x * pre_num
                    pre_num += x

        return ans - num_parallelogram // 2


class Solution:
    # 灵神
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))  # 斜率 -> 截距 -> 个数
        cnt2 = defaultdict(lambda: defaultdict(int))  # 中点 -> 斜率 -> 个数

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else inf
                b = (y * dx - x * dy) / dx if dx else x
                cnt[k][b] += 1  # 按照斜率和截距分组
                cnt2[(x + x2, y + y2)][k] += 1  # 按照中点和斜率分组

        ans = 0
        for m in cnt.values():
            s = 0
            for c in m.values():
                ans += s * c
                s += c

        for m in cnt2.values():
            s = 0
            for c in m.values():
                ans -= s * c  # 平行四边形会统计两次，减去多统计的一次
                s += c

        return ans  # 2145ms
    
class Solution:
    # 灵神
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(list)  # 斜率 -> [截距]
        groups2 = defaultdict(list)  # 中点 -> [斜率]

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else inf
                b = (y * dx - x * dy) / dx if dx else x
                groups[k].append(b)
                groups2[(x + x2, y + y2)].append(k)

        ans = 0
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans += s * c
                s += c

        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c  # 平行四边形会统计两次，减去多统计的一次
                s += c

        return ans  # 1191ms

fun = Solution()
fun.countTrapezoids([[-3,2],[2,3],[3,2],[2,-3]])
            