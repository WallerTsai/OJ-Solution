from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List
from sortedcontainers import SortedList


class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.memory = 0
        self.FIFO = deque()
        self.visited = set()
        self.destination_to_timelist = defaultdict(SortedList)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.visited:
            return False
        
        self.memory += 1
        self.FIFO.append((source, destination, timestamp))
        self.visited.add((source, destination, timestamp))
        self.destination_to_timelist[destination].add(timestamp)

        if self.memory > self.limit:
            self.forwardPacket()

        return True

    def forwardPacket(self) -> List[int]:
        if self.memory:
            s, d, t = self.FIFO.popleft()
            self.visited.remove((s, d, t))
            self.destination_to_timelist[d].remove(t)
            self.memory -= 1
            return [s, d, t]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return self.destination_to_timelist[destination].bisect_right(endTime) - self.destination_to_timelist[destination].bisect_left(startTime)

# 由于题目 对于 addPacket 的查询会按照 timestamp 的递增顺序进行
# 所以不需要特意排序
class Router:
    # 灵神
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_q = deque()  # packet 队列
        self.packet_set = set()  # packet 集合
        self.dest_to_timestamps = defaultdict(deque)  # destination -> [timestamp]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        if len(self.packet_q) == self.memory_limit:  # 太多了
            self.forwardPacket()
        self.packet_q.append(packet)  # 入队
        self.dest_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_q:
            return []
        packet = self.packet_q.popleft()  # 出队
        self.packet_set.remove(packet)
        self.dest_to_timestamps[packet[1]].popleft()
        return packet  # list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_to_timestamps[destination]
        left = bisect_left(timestamps, startTime)  # deque 访问不是 O(1) 的，可以看另一份代码【Python3 list】
        right = bisect_right(timestamps, endTime)
        return right - left