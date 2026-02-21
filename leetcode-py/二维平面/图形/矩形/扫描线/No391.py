from bisect import bisect_left
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    # 条件：
    # 1. 最边缘四个点构成的矩形的面积 == 全部矩形面积和
    # 2. 每个矩形的顶点出现次数和一定是2 或 4 (除了最边缘的四个)
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        mx1, my1, mx2, my2 = rectangles[0]
        cnt = defaultdict(int)

        for rec in rectangles:
            x1, y1, x2, y2 = rec

            area += (x2 - x1) * (y2 - y1)

            mx1 = min(mx1, x1)
            my1 = min(my1, y1)
            mx2 = max(mx2, x2)
            my2 = max(my2, y2)

            cnt[x1, y1] += 1
            cnt[x1, y2] += 1
            cnt[x2, y1] += 1
            cnt[x2, y2] += 1

        if (mx2 - mx1) * (my2 - my1) != area:
            return False
 
        if cnt[mx1, my1] * cnt[mx1, my2] * cnt[mx2, my1] * cnt[mx2, my2] != 1:
            return False
        
        del cnt[mx1, my1], cnt[mx1, my2], cnt[mx2, my1], cnt[mx2, my2]

        return all(x == 2 or x == 4 for x in cnt.values())  # 39ms


class Solution:
    # 扫描线
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y, max_x, max_y = rectangles[0]

        # 定义事件：(x, 边界类型, y1, y2)
        # 技巧：出场设为 -1，入场设为 1。在 x 相同时，-1 排在 1 前面，先删后加。
        events = []
        for x1, y1, x2, y2 in rectangles:
            # min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        events.sort()

        active_intervals = []

        i = 0
        n = len(events)
        while i < n:
            cur_x = events[i][0]
            
            while i < n and events[i][0] == cur_x:
                x, t, y1, y2 = events[i]

                if t == 1:
                    # 查找插入位置
                    idx = bisect_left(active_intervals, (y1, y2))
                    
                    # 检查与前一个区间重叠
                    if idx > 0 and active_intervals[idx - 1][1] > y1:
                        return False
                    
                    # 检查与后一个区间重叠
                    if idx < len(active_intervals) and active_intervals[idx][0] < y2:
                        return False
                    
                    active_intervals.insert(idx, (y1, y2))
                else:
                    active_intervals.remove((y1, y2))

                i += 1

            if cur_x == max_x:
                break

            # 检查连续性
            if not active_intervals:
                return False
            if active_intervals[0][0] != min_y or active_intervals[-1][1] != max_y: # 底部和顶部对齐
                return False
            for j in range(1, len(active_intervals)):   # 中间对齐
                if active_intervals[j][0] != active_intervals[j - 1][1]:
                    return False

        return True # 867ms
    

# gemini 解法： 线段树 + 扫描线
class SegmentTree:
    def __init__(self, y_coords):
        self.y = y_coords
        self.n = len(y_coords) - 1
        self.cnt = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)
        self.has_overlap = False

    def _update_node(self, node, l, r):
        if self.cnt[node] > 0:
            # 如果被完全覆盖
            self.length[node] = self.y[r + 1] - self.y[l]
        elif l < r:
            # 否则等于子节点覆盖长度之和
            self.length[node] = self.length[2 * node] + self.length[2 * node + 1]
        else:
            self.length[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if self.has_overlap: return
        
        if ql <= l and r <= qr:
            self.cnt[node] += val
            # 完美矩形关键：如果任何节点被覆盖超过1次，即为重叠
            if self.cnt[node] > 1:
                self.has_overlap = True
            self._update_node(node, l, r)
            return

        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        self._update_node(node, l, r)
        # 额外重叠检查：如果子区间都满了且当前又要加，也会产生重叠
        # 但在完美矩形逻辑中，通过 cnt[node] > 1 和面积校验已足够

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        if not rectangles: return False
        
        # 1. 坐标离散化 y 轴
        y_set = set()
        area_sum = 0
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            y_set.add(y1)
            y_set.add(y2)
            area_sum += (x2 - x1) * (y2 - y1)
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
        
        # 2. 面积前置检查 (O(N) 快速排除)
        if area_sum != (max_x - min_x) * (max_y - min_y):
            return False
        
        # 离散化映射
        sorted_y = sorted(list(y_set))
        y_map = {val: i for i, val in enumerate(sorted_y)}
        
        # 3. 准备事件
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))  # 入场
            events.append((x2, -1, y1, y2)) # 出场
        
        # 按 x 排序，x 相同则先处理出场(-1)再处理入场(1)
        # 注意：对于完美矩形，x相同时先-1还是先1取决于你的逻辑，
        # 这里的面积校验+len校验允许我们直接按坐标处理。
        events.sort()
        
        tree = SegmentTree(sorted_y)
        total_h = max_y - min_y
        
        i = 0
        while i < len(events):
            curr_x = events[i][0]
            # 处理当前 x 的所有边
            while i < len(events) and events[i][0] == curr_x:
                _, type, y1, y2 = events[i]
                tree.update(1, 0, tree.n - 1, y_map[y1], y_map[y2] - 1, type)
                if tree.has_overlap: return False
                i += 1
            
            # 检查当前 y 轴覆盖长度
            # 如果不是终点，且覆盖长度不等于总高度，说明有空隙或重叠
            if curr_x < max_x:
                if tree.length[1] != total_h:
                    return False
            else:
                if tree.length[1] != 0:
                    return False
                    
        return True # 267ms
    


from sortedcontainers import SortedList # type: ignore 
# sl + 扫描线
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 1. 计算大矩形的理论边界和总面积
        min_x, min_y, max_x, max_y = rectangles[0]

        events = []
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        events.sort()

        active_intervals = SortedList()
        curr_total_height = 0
        expected_height = max_y - min_y
        
        i = 0
        n = len(events)
        while i < n:
            curr_x = events[i][0]
            

            while i < n and events[i][0] == curr_x:
                x, t, y1, y2 = events[i]
                if t == 1:
                    # 入场：检查重叠并维护总高度
                    # bisect_left 返回插入位置，其左右即为可能重叠的邻居
                    idx = active_intervals.bisect_left((y1, y2))
                    
                    # 检查左侧：邻居的 y2 是否超过了我的 y1
                    if idx > 0 and active_intervals[idx-1][1] > y1:
                        return False
                    # 检查右侧：邻居的 y1 是否小于了我的 y2
                    if idx < len(active_intervals) and active_intervals[idx][0] < y2:
                        return False
                    
                    active_intervals.add((y1, y2))
                    curr_total_height += (y2 - y1)
                else:
                    # 出场：移除并减去高度
                    active_intervals.remove((y1, y2))
                    curr_total_height -= (y2 - y1)
                i += 1
            
            # 连续性校验
            # 只要不是在起始点或终点，中间任何位置的总高度必须等于预期高度
            if curr_x < max_x:
                if curr_total_height != expected_height:
                    return False
                    
        return True # 107ms