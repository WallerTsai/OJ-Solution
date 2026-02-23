# 贪心
# 难度：中等
from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        differ = []
        # 求出每个背包的空额
        for i in range(len(capacity)):
            differ.append(capacity[i]-rocks[i])
        differ.sort()
        for j in range(len(differ)):
            additionalRocks -= differ[j]
            if additionalRocks < 0:
                break
            res += 1
        return res  # 66ms

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        differ = []
        # 求出每个背包的空额
        for i in range(len(capacity)):
            differ.append(capacity[i]-rocks[i])
        differ.sort()
        for j in differ:
            if j == 0:
                res += 1
                continue

            additionalRocks -= j
            if additionalRocks < 0:
                break
            res += 1
        return res  # 59ms
    
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        differ = [0]*len(capacity)
        # 求出每个背包的空额
        for i in range(len(capacity)):
            differ[i] = capacity[i]-rocks[i]
        differ.sort()
        for j in differ:
            if j == 0:
                res += 1
                continue

            additionalRocks -= j
            if additionalRocks < 0:
                break
            res += 1
        return res  # 55ms
    
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = [cap - rock for cap, rock in zip(capacity, rocks)]  # 计算每个背包还能装多少石头
        if sum(diffs) <= additionalRocks:  # 如果额外的石头足够填满所有背包
            return len(capacity)
        
        diffs.sort()  # 对差值进行排序
        ans = 0
        for diff in diffs:
            if additionalRocks >= diff:  # 如果额外的石头足够填满当前背包
                additionalRocks -= diff  # 使用石头
                ans += 1  # 背包数量加一
            else:
                break  # 如果石头不够了，就退出循环
        return ans  # 33ms