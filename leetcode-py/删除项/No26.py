from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #第一个值必须保留,所以标记和循环从下标1开始
        flat_index = 1 #标记节点
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[flat_index] = nums[i]
                flat_index += 1
        return flat_index

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums)) #注意这里一定得在原来列表那要加[:]
        return len(nums)