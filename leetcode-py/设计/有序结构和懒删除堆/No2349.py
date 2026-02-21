from collections import defaultdict
from heapq import heappop, heappush


class NumberContainers:

    def __init__(self):
        self.index_to_number = dict()
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        old_number = self.index_to_number.get(index, None)
        if old_number is not None:
            self.number_to_indices[old_number].discard(index)

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        return indices[0] if indices else - 1
    

class NumberContainers:
    # 有序集合
    def __init__(self):
        self.index_to_number = {}
        # from sortedcontainers import SortedSet
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        # 移除旧数据
        old_number = self.index_to_number.get(index, None)
        if old_number is not None:
            self.number_to_indices[old_number].discard(index)

        # 添加新数据
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        return indices[0] if indices else -1
    

class NumberContainers:
    # 懒删除堆
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # 添加新数据
        self.index_to_number[index] = number
        heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        while indices and self.index_to_number[indices[0]] != number:
            heappop(indices)  # 堆顶货不对板，说明是旧数据，删除
        return indices[0] if indices else -1