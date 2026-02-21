from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        n = length // 3

        # 可以预处理
        suf_list = nums[2 * n: ]
        suf_sum = sum(suf_list)
        heapq.heapify(suf_list)

        pre_list = [-x for x in nums[:n]]
        pre_sum = -sum(pre_list)
        heapq.heapify(pre_list)

        ans = pre_sum - suf_sum

        hash_dict = defaultdict(int)
        hash_dict[2 * n] = suf_sum

        # 后缀最大和
        for i in range(2 * n - 1, n - 1, -1):
            suf_sum += nums[i] - heapq.heappushpop(suf_list, nums[i]) # 注意这个方法, 先进堆再弹出最小
            hash_dict[i] = suf_sum


        # 前缀最小值 + 更新结果
        for i in range(n, 2 * n):
            pre_sum -=  (-heapq.heappushpop(pre_list, -nums[i])) - nums[i]
            ans = min(ans, pre_sum - hash_dict[i + 1])

        return ans
    
    
fun = Solution()
print(fun.minimumDifference([16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]))

# 上面这段代码在尝试监视某些值时会导致ans不更新
# 同时 上面代码存在问题, 没有AC

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        n = length // 3

        # 可以预处理
        suf_list = nums[2 * n: ]
        suf_sum = sum(suf_list)
        heapq.heapify(suf_list)

        pre_list = [-x for x in nums[:n]]
        pre_sum = -sum(pre_list)
        heapq.heapify(pre_list)

        hash_dict = defaultdict(int)
        hash_dict[2 * n] = suf_sum

        # 后缀最大和
        for i in range(2 * n - 1, n - 1, -1):
            suf_sum += nums[i] - heapq.heappushpop(suf_list, nums[i]) # 注意这个方法, 先进堆再弹出最小
            hash_dict[i] = suf_sum

        ans = pre_sum - hash_dict[n]
        # 前缀最小值 + 更新结果
        for i in range(n, 2 * n):
            pre_sum -=  (-heapq.heappushpop(pre_list, -nums[i])) - nums[i]
            ans = min(ans, pre_sum - hash_dict[i + 1])

        return ans