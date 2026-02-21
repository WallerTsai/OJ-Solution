from collections import defaultdict
from itertools import pairwise
from math import inf
from typing import List
    
class Solution:
    # 二分
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        y_min = inf
        y_max = 0

        for _,y,l in squares:
            # 这里非常浪费时间
            total += l ** 2
            y_min = min(y_min,y)
            y_max = max(y_max,y+l)

        def area(i:int):
            s = 0
            for _,y,l,in squares:
                if y + l <= i:
                    s += l ** 2
                elif y < i < y + l:
                    s += (i-y) * l
            return s
        
        while y_max - y_min > 1e-5:
            y_mid = (y_max + y_min) / 2
            s_below = area(y_mid)
            if s_below < total / 2:
                y_min = y_mid
            else:
                y_max = y_mid
        
        return y_min # 2426ms

class Solution:
    # 灵神
    # 差分
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot_area = 0
        diff = defaultdict(int)
        for _, y, l in squares:
            tot_area += l * l
            diff[y] += l
            diff[y + l] -= l

        area = sum_l = 0
        for y, y2 in pairwise(sorted(diff)):
            sum_l += diff[y]  # 矩形底边长度之和
            tmp = area + sum_l * (y2 - y)  # 底边长 * 高 = 新增面积
            if tmp * 2 >= tot_area:
                return y + (tot_area / 2 - area) / sum_l
            area = tmp # 326ms



# 2026年1月13日

from collections import defaultdict
from itertools import pairwise
from math import sqrt
from typing import List


class Solution:
    # 浮点二分
    def separateSquares(self, squares: List[List[int]]) -> float:
        eps = 1e-5 # 由于是浮点数运算，允许使用e

        max_y = total_area = 0
        for _, y, l in squares:
            total_area += pow(l, 2)
            if y + l > max_y:
                max_y = y + l

        def check(limit_y: float):
            area = 0
            for _, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2
        
        lo, hi =  0, max_y
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi   # 1841ms


class Solution:
    # 差分
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        diff = defaultdict(int)

        for x, y, l in squares:
            total_area += pow(l, 2)
            diff[y] += l
            diff[y + l] -= l

        area = base_width = 0
        for y1, y2 in pairwise(sorted(diff.keys())):
            base_width += diff[y1]
            temp_area = area + base_width * (y2 - y1)
            if temp_area >= total_area / 2:
                return y1 + (total_area / 2 - area) / base_width
            area = temp_area    # 287ms


class Solution:
    # leetcode 官方
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        events = []
        
        for sq in squares:
            y, l = sq[1], sq[2]
            total_area += l * l
            events.append((y, l, 1))
            events.append((y + l, l, -1))
        
        # 按y坐标排序
        events.sort(key=lambda x: x[0])
        
        covered_width = 0.0  # 当前扫描线下所有底边之和
        curr_area = 0.0      # 当前累计面积
        prev_height = 0.0    # 前一个扫描线的高度
        
        for y, l, delta in events:
            diff = y - prev_height
            # 两条扫描线之间新增的面积
            area = covered_width * diff
            # 如果加上这部分面积超过总面积的一半
            if 2 * (curr_area + area) >= total_area:
                return prev_height + (total_area - 2 * curr_area) / (2 * covered_width) # 这里可以改成：(total_area / 2 - area) / base_width 但是官解更加严谨，那样可以避免精度损失
            # 更新宽度：开始事件加宽度，结束事件减宽度
            covered_width += delta * l
            curr_area += area
            prev_height = y
        
        return 0.0