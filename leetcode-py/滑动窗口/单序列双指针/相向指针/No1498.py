# 进行数学分析
# 结合相向双指针
# 发现是 二项式定理 问题
# 在排序后固定左指针后，对于左指针到右指针，除左指针的元素都有 选和不选两种情况


from typing import List
MOD =  10 ** 9 + 7

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += pow(2,right - left)
                left += 1
            else:
                right -= 1
        
        return ans % MOD    # 7159ms

# 灵神
# 预处理 pow
MOD = 1_000_000_007
MX = 100_000

pow2 = [1] * MX  # pow2[i] = 2 ** i % MOD
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:  # 可以相等，此时子序列的最小最大是同一个数
            if nums[left] + nums[right] <= target:
                # nums[left] 可以作为子序列的最小值
                # 其余下标在 [left+1,right] 中的数选或不选都可以
                ans += pow2[right - left]
                left += 1
            else:
                # nums[right] 太大了，即使与剩余元素的最小值 nums[left] 相加也不满足要求
                right -= 1
        return ans % MOD    # 90ms
