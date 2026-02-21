from collections import deque
from typing import List


class Solution:
    # 暴力
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        for i in range(length):
            for j in range(i+1,length):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
                
        return res # 超时

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        dq = []
        for i in range(length-1,-1,-1):
            while dq:
                if temperatures[i] >= dq[-1][1]:
                    dq.pop()
                else:
                    res[i] = dq[-1][0] - i
                    break
            dq.append((i,temperatures[i]))
        return res  # 142ms

class Solution:
    # leetcode 最快
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n-2, -1, -1):
            compare = i+1
            while temperatures[i] >= temperatures[compare]:
                if res[compare] == 0:
                    break
                else:
                    compare += res[compare]
            else:
                res[i] = compare - i
        return res