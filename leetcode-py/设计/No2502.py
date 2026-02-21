class Allocator:

    def __init__(self, n: int):
        self.total_size = n
        self._data = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        left = 0
        flag = False
        for right,id in enumerate(self._data):
            if id != 0:
                left = right + 1
            else:
                if right - left + 1 == size:
                    flag = True
                    break
        
        if flag:
            for i in range(left,left + size):
                self._data[i] = mID
            return left
        else:
            return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i,n in enumerate(self._data):
            if n == mID:
                self._data[i] = 0
                count += 1
        return count    # 941ms
    
class Allocator:
    # leetcode 大佬
    def __init__(self, n: int):
        # 初始化内存的空闲区间为从 0 到 n-1
        self.free_intervals = [(0, n-1)]  # 每个区间是 (start, end)
        self.mID_map = {}  # 记录 mID 与占用的区间的对应关系

    def allocate(self, size: int, mID: int) -> int:
        # 尝试分配 size 大小的内存
        for i, (start, end) in enumerate(self.free_intervals):
            if end - start + 1 >= size:  # 找到足够大的空闲区间
                # 更新空闲区间
                allocated_start = start
                allocated_end = start + size - 1
                remaining_start = allocated_end + 1
                remaining_end = end

                # 记录该 mID 对应的分配区间
                if mID not in self.mID_map:
                    self.mID_map[mID] = []
                self.mID_map[mID].append((allocated_start, allocated_end))

                # 删除原来的区间，添加新的区间
                self.free_intervals.pop(i)
                if remaining_start <= remaining_end:  # 如果剩余的空间有效
                    self.free_intervals.insert(i, (remaining_start, remaining_end))

                # 按照区间的起始位置排序
                self.free_intervals.sort()

                return allocated_start
        return -1  # 没有找到合适的空闲区间

    def freeMemory(self, mID: int) -> int:
        # 释放给定 mID 的所有内存单元
        if mID not in self.mID_map:
            return 0

        total_freed = 0
        # 获取并释放所有分配给 mID 的区间
        for start, end in self.mID_map[mID]:
            # 释放这些区间，恢复为空闲区间
            total_freed += end - start + 1
            self.free_intervals.append((start, end))

        # 清空该 mID 的记录
        del self.mID_map[mID]

        # 按照区间的起始位置排序
        self.free_intervals.sort()

        # 合并相邻的空闲区间
        merged_intervals = []
        for start, end in self.free_intervals:
            if not merged_intervals or merged_intervals[-1][1] < start - 1:
                merged_intervals.append((start, end))
            else:
                merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], end))
        self.free_intervals = merged_intervals

        return total_freed # 16ms


# 有序列表
from collections import defaultdict
from sortedcontainers import SortedList
class Allocator:
# 作者：wxyz
    def __init__(self, n: int):
        # 每个内存块表示为 [start, end, mID]，其中 mID=0 表示空闲，升序
        self.memory_blocks = SortedList([(0, 0, 0), (n, n, 0)])  # 增加两个哨兵
    
    def allocate(self, size: int, mID: int) -> int:
        # 从前往后遍历
        for i in range(len(self.memory_blocks) - 1):
            prev_block = self.memory_blocks[i]
            next_block = self.memory_blocks[i + 1]
            # 计算当前空闲区域大小
            free_space = next_block[0] - prev_block[1]
            # 找到足够大的空闲区域，分配内存
            if free_space >= size:
                new_block = (prev_block[1], prev_block[1] + size, mID)
                self.memory_blocks.add(new_block)
                return prev_block[1]  # 返回分配的起始地址
        return -1  # 没有足够大的空闲区域，返回 -1

    def freeMemory(self, mID: int) -> int:
        free_size = 0
        # 遍历所有内存块，释放所有 mID 对应的内存块
        blocks_to_remove = []
        for block in self.memory_blocks:
            if block[2] == mID:
                # 记录需要释放的内存块
                free_size += block[1] - block[0]
                blocks_to_remove.append(block)
        # 移除所有需要释放的内存块
        for block in blocks_to_remove:
            self.memory_blocks.remove(block)
        return free_size  # 返回释放的总内存大小

# 手动维护
class Allocator:
# 作者：wxyz
    def __init__(self, n: int):
        # 每个内存块表示为 [start, end, mID]，其中 mID=0 表示空闲，升序
        self.memory_blocks = [[0, 0, 0], [n, n, 0]]  # 增加两个哨兵
    
    def allocate(self, size: int, mID: int) -> int:
        # 从前往后遍历
        for i in range(len(self.memory_blocks) - 1):
            prev_block = self.memory_blocks[i]
            next_block = self.memory_blocks[i + 1]
            free_space = next_block[0] - prev_block[1]
            if free_space >= size:
                new_block = [prev_block[1], prev_block[1] + size, mID]
                # 只修改这一个地方！
                self.memory_blocks.insert(i + 1, new_block)
                return prev_block[1]  # 返回分配的起始地址
        return -1

    def freeMemory(self, mID: int) -> int:
        free_size = 0
        # 从后向前遍历！
        for i in range(len(self.memory_blocks) - 1, -1, -1):
            block = self.memory_blocks[i]
            if block[2] == mID:
                free_size += block[1] - block[0]
                # 可以直接释放！
                self.memory_blocks.pop(i)
        return free_size

# 区间修改
class Allocator:
# 作者：wxyz
    def __init__(self, n: int):
        # 空闲内存块列表
        self.free_blocks = [(0, n)]
        # 使用字典记录每个 mID 分配的内存块
        self.allocated_blocks = defaultdict(list)
    
    def allocate(self, size: int, mID: int) -> int:
        # 遍历空闲内存块，寻找足够大的区域
        for i, (start, end) in enumerate(self.free_blocks):
            if end - start < size:
                continue  # 当前空闲块不够大，跳过
            if end - start == size:
                # 如果空闲块大小正好等于需求，直接移除
                del self.free_blocks[i]
            else:
                # 否则，缩小空闲块的范围
                self.free_blocks[i] = (start + size, end)
            # 记录分配的内存块
            self.allocated_blocks[mID].append((start, start + size))
            return start  # 返回分配的起始地址
        return -1  # 没有足够大的空闲块，返回 -1

    def freeMemory(self, mID: int) -> int:
        free_size = 0
        # 获取并移除 mID 对应的所有内存块
        blocks_to_free = self.allocated_blocks.pop(mID, [])
        # 计算释放的内存大小，并将释放的内存块加入空闲列表
        for start, end in blocks_to_free:
            free_size += end - start
            self.free_blocks.append((start, end))
        # 对空闲内存块进行排序和合并
        self.free_blocks.sort()
        merged_blocks = []
        for block in self.free_blocks:
            if merged_blocks and merged_blocks[-1][1] == block[0]:
                # 如果当前块与前一个块相邻，合并它们
                merged_blocks[-1] = (merged_blocks[-1][0], block[1])
            else:
                # 否则，直接添加当前块
                merged_blocks.append(block)
        self.free_blocks = merged_blocks
        return free_size  # 返回释放的总内存大小


obj = Allocator(10)
param_1 = obj.allocate(1,1)
param_2 = obj.allocate(1,2)
param_2 = obj.allocate(1,3)
param_2 = obj.freeMemory(2)
param_2 = obj.allocate(3,4)
param_2 = obj.allocate(1,1)
param_2 = obj.allocate(1,1)
param_2 = obj.freeMemory(1)
print(param_2)
# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)