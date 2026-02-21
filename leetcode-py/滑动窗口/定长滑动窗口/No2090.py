from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        length = len(nums)
        res = [-1] * length

        if 2 * k >= length:
            return res
        
        cur_sum = sum(nums[:2*k+1])
        res[k] = cur_sum // (2*k+1)

        for i in range(k+1,length-k):
            cur_sum = cur_sum + nums[i+k] - nums[i-k-1]
            res[i] = cur_sum // (2*k+1)

        return res  # 51ms

class Solution(object):
    def getAverages(self, nums, k):

        mark=0
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            mark+=nums[i]
            if i<2*k:
                continue
            res[i-k]=mark//(2*k+1) 
            mark-=nums[i-2*k]
        return res  # 127ms

