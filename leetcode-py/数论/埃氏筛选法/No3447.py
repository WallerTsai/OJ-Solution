from math import inf
from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        length = len(groups)
        path = []
        hash = dict()
        for group in groups:
            num = -1
            if group in hash:
                path.append(hash[group])
                continue
            for i,e in enumerate(elements):
                if group % e == 0:
                    num = i
                    break
            hash[group] = num
            path.append(num)
        return path # 超时
    
MX = 100001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        length = len(groups)
        path = []
        hash = dict()
        ele = dict()
        for i,e in enumerate(elements):
            if e not in ele:
                ele[e] = i

        for group in groups:
            num = inf
            if group in hash:
                path.append(hash[group])
                continue
            for x in divisors[group]:
                if x in ele:
                    num = min(num,ele[x])
            if num == inf:
                num = -1
            hash[group] = num
            path.append(num)
        return path # 1111ms
    
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        length = len(elements)
        
        # 筛选统计elements
        idx = {elements[i]: i for i in range(length-1,-1,-1)}

        # 预处理mx以内的因素
        mx = max(groups)
        target = [inf] * (mx + 1)
        for x,i in idx.items():
            for y in range(x,mx+1,x):
                target[y] = min(target[y],i)

        # 更新答案
        for i,x in enumerate(groups):
            j = target[x]
            groups[i] = -1 if j == inf else j

        return groups   # 658ms

class Solution:
    # 灵神
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        target = [-1] * (mx + 1)
        for i, x in enumerate(elements):
            if x > mx or target[x] >= 0:  # x 及其倍数已被标记
                continue
            for y in range(x, mx + 1, x):  # 枚举 x 的倍数 y
                if target[y] < 0:
                    target[y] = i  # 标记 y 可以被 x 整除
        return [target[x] for x in groups]  # 回答询问