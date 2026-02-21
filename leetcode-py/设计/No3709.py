from bisect import bisect_left, bisect_right
from collections import defaultdict


class ExamTracker:

    def __init__(self):
        self.score_pre_list = [0]
        self.time_list = []

    def record(self, time: int, score: int) -> None:
        self.score_pre_list.append(self.score_pre_list[-1] + score)
        self.time_list.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect_left(self.time_list, startTime)
        right = bisect_right(self.time_list, endTime)
        return self.score_pre_list[right] - self.score_pre_list[left]
    
[1, 2, 3]
[0, 1, 3, 6]
[1, 2, 3]