from collections import Counter, defaultdict
from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        temp_list = nums[:k]
        cur_sum = sum(temp_list)
        count = len(set(temp_list))


        res = cur_sum if count >= m else 0

        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            temp_list.append(nums[i])
            temp_list.pop(0)
            if len(set(temp_list)) >= m:
                res = max(res,cur_sum)

        return res  # 5852ms

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cur_sum = sum(nums[:k])
        count = len(set(nums[:k]))


        res = cur_sum if count >= m else 0

        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if nums[i] not in nums[i-k:i]:
                count += 1
            if nums[i-k] not in nums[i-k+1:i+1]:
                count -= 1
            if count >= m:
                res = max(res,cur_sum)

        return res  #3755ms

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cur_sum = sum(nums[:k])
        count = len(set(nums[:k]))

        res = cur_sum if count >= m else 0

        for i in range(k,len(nums)):
            if nums[i] not in nums[i-k:i]:
                count += 1
            if nums[i-k] not in nums[i-k+1:i+1]:
                count -= 1
            if count >= m and sum(nums[i-k+1:i+1]) > res:
                res = sum(nums[i-k+1:i+1])

        return res  # 5760ms

class Solution:
# 作者：灵茶山艾府
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        s = sum(nums[:k - 1])  # 先统计 k-1 个数
        cnt = Counter(nums[:k - 1])
        for out, in_ in zip(nums, nums[k - 1:]):
            s += in_  # 再添加一个数就是 k 个数了
            cnt[in_] += 1
            if len(cnt) >= m:
                ans = max(ans, s)

            s -= out  # 下一个子数组不包含 out，移出窗口
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans  # 163ms

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        the_dict = defaultdict(int)
        res = 0
        cur_sum = 0
        
        for i,num in enumerate(nums):
            cur_sum += num
            the_dict[num] += 1

            if i < k-1:
                continue

            if len(the_dict) >= m and cur_sum > res:
                res = cur_sum

            cur_sum -= nums[i-k+1]
            the_dict[nums[i-k+1]] -= 1
            if the_dict[nums[i-k+1]] == 0:
                del the_dict[nums[i-k+1]]

        return res  # 107ms

