from collections import defaultdict
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = sum(nums[:k])
        count = len(set(nums[:k]))
        res = cur_sum if count==k else 0

        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if nums[i-k] not in nums[i-k+1:i]:
                count -= 1
            if nums[i] not in nums[i-k+1:i]:
                count += 1
                if count == k and cur_sum > res:
                    res = cur_sum
        
        return res  # 超时

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = sum(nums[:k])
        count = len(set(nums[:k]))
        res = cur_sum if count==k else 0

        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if len(set(nums[i-k+1:i+1])) == k and cur_sum > res:
                res = cur_sum

        return res  #超时

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        the_dict = defaultdict(int)
        res = 0 
        cur_sum = 0

        for i,num in enumerate(nums):
            cur_sum += num
            the_dict[num] += 1

            if i < k-1:
                continue

            if len(the_dict) == k and cur_sum > res:
                res = cur_sum

            cur_sum -= nums[i-k+1]
            the_dict[nums[i-k+1]] -= 1
            if the_dict[nums[i-k+1]] == 0:
                del the_dict[nums[i-k+1]]

        return res  #159ms - 240ms

class Solution:
    # leetcode 最快
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        current_sum = 0
        max_sum = 0
        begin = 0

        for end in range(n):
            if nums[end] not in elements:
                current_sum += nums[end]
                elements.add(nums[end])

                if end - begin + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
                    
                begin += 1
                
        return max_sum  
