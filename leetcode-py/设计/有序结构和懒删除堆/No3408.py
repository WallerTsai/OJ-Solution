from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = dict()
        self.task_to_priority = dict()
        self.li = []
        for task in tasks:
            userid, taskid, p = task
            self.task_to_user[taskid] = userid
            self.task_to_priority[taskid] = p
            heappush(self.li, (-p, -taskid, userid))


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        heappush(self.li, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        userId = self.task_to_user[taskId]
        heappush(self.li, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.task_to_user[taskId]
        del self.task_to_priority[taskId]

    def execTop(self) -> int:
        while self.li:
            value = heappop(self.li)
            p, taskId, userId = -value[0], -value[1], value[2]
            if taskId not in self.task_to_user:
                continue
            if userId != self.task_to_user[taskId] or p != self.task_to_priority[taskId]:
                continue
            return userId
        return -1

# 上面代码漏洞在 正确的任务执行后没有删除记录

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = dict()
        self.task_to_priority = dict()
        self.li = []
        for task in tasks:
            userid, taskid, p = task
            self.task_to_user[taskid] = userid
            self.task_to_priority[taskid] = p
            heappush(self.li, (-p, -taskid, userid))


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        heappush(self.li, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        userId = self.task_to_user[taskId]
        heappush(self.li, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.task_to_user[taskId]
        del self.task_to_priority[taskId]

    def execTop(self) -> int:
        while self.li:
            value = heappop(self.li)
            p, taskId, userId = -value[0], -value[1], value[2]
            if taskId not in self.task_to_user:
                continue
            if userId != self.task_to_user[taskId] or p != self.task_to_priority[taskId]:
                continue
            self.rmv(taskId)
            return userId
        return -1   # 583ms