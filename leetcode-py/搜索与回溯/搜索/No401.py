from typing import List


class Solution:
    # 枚举
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res


class Solution:
    # 郁郁雨大佬
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []
        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append('%d:%02d' % (hour, minute))
                return
            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])
        
        backtrack(num, 0, 0, 0)
        return res
    

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        hours_map = [1, 2, 4, 8]
        minutes_map = [1, 2, 4, 8, 16, 32]

        def backtrack(count, start, h, m):
            if h >= 12 or m >= 60:
                return
            
            if count == turnedOn:
                res.append(f"{h}:{m:02d}")
                return
            
            for i in range(start, 10):
                if i < 4:
                    backtrack(count + 1, i + 1, h + hours_map[i], m)
                else:
                    backtrack(count + 1, i + 1, h, m + minutes_map[i - 4])

        backtrack(0, 0, 0, 0)
        return res