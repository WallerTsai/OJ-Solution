from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = nums[0]
        right = nums[k + 1]
        left_l = right_l = 0
        res = []

        for i in range(k, n - 1):
            if nums[i - k] <= left:
                left_l += 1
            else:
                left_l = 1
            
            if nums[i + 1] >= right:
                right_l += 1
            else:
                right_l = 1

            if left_l >= k and right_l >= k:
                res.append(i - k + 1)

            left = nums[i - k]
            right = nums[i + 1]

        return res  # 63ms


class Solution:
    # gemini
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # before[i] 表示到 i 位置为止，连续非递增的元素个数
        before = [1] * n
        # after[i] 表示从 i 位置开始，连续非递减的元素个数
        after = [1] * n
        
        # 1. 预处理左侧：非递增 (nums[i] <= nums[i-1])
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                before[i] = before[i-1] + 1
        
        # 2. 预处理右侧：非递减 (nums[i] <= nums[i+1])
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                after[i] = after[i+1] + 1
        
        res = []
        # 3. 检查好下标：下标 i 需要满足 i-1 位置有 k 个非递增，i+1 位置有 k 个非递减
        # 下标范围：k <= i < n - k
        for i in range(k, n - k):
            if before[i-1] >= k and after[i+1] >= k:
                res.append(i)
                
        return res
