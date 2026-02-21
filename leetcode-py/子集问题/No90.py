from functools import cache
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        path = []
        def dfs(i:int):
            if i == length:
                if path not in res:
                    res.append(path[:])
                return
            # 选
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            # 不选
            dfs(i+1)
            return
        dfs(0)
        return res  #7ms 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []

        def dfs(i:int,path:list):
            if i == length:
                if path not in res:
                    res.append(path[:])
                return
            # 选
            dfs(i+1,path=path + [nums[i]])

            # 不选
            dfs(i+1,path)
            return
        dfs(0,[])
        return res  # 3ms
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        path = []
        def dfs(i:int):
            res.append(path[:])
            for x in range(i,length):
                if x != i and nums[x] == nums[x-1]:
                    continue
                path.append(nums[i])
                dfs(x+1)
                path.pop()

        dfs(0)
        return res  # 0ms
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        path = []
        def dfs(i:int):
            if i == length:
                if path not in res:
                    res.append(path[:])
                return
            # 选
            temp = nums[i]
            path.append(temp)
            dfs(i+1)
            path.pop()
            # 不选
            i += 1
            while i < length and nums[i] == temp:
                i += 1
            dfs(i)

        dfs(0)
        return res