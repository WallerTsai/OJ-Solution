
from collections import defaultdict
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        pre_max = 0
        n = len(nums)
        ans = nums[:]

        pre_li = []
        for num in nums:
            pre_max = max(pre_max, num)
            pre_li.append(pre_max)

        st = []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            MX = pre_li[i]

            while st and (st[-1][0] >= num or st[-1][1] <= MX):
                st.pop()

            st.append([num, MX])

            temp_st = st[:]
            temp = -1
            while temp_st and num >= temp_st[-1][0]:
                t = temp_st.pop()
                temp = t[1]

            ans[i] = max(MX, temp)

        return ans  # 错误
    

# 设 f(i) 表示前 i 个元素的最大值，g(i) 表示第 i 到第 n 个元素的最小值。

# 因为往后跳只能往更小的数走，所以如果 f(i)≤g(i+1)，那么前 i 个数不可能到达后面的数。然后注意到每次跳跃都是双向可通行的，所以后面的数也到不了前面的数。

# 反之，如果 f(i)>g(i+1)，那么第 i 个数可以先跳到前面的最大值 f(i)，然后跳到后面的最小值 g(i+1)，然后再跳到第 (i+1) 个数。同样由于每次跳跃都是双向可通行的，第 (i+1) 个数也可以反过来到第 i 个数。

# 因此，每个 f(i)≤g(i+1) 的位置就把整个序列分成了很多段，每一段的答案就是当前段的最大值。

# 作者：TsReaper

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        suf_min = inf
        mx = 0
        for i in range(n - 1, -1, -1):
            if pre_max[i] <= suf_min:
                mx = pre_max[i]  # 无法跳到 [i+1,n-1] 中，只能跳到 [0,i] 中的最大值
            suf_min = min(suf_min, nums[i])
            nums[i] = mx
        return nums
    


# 2026年5月7日
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = list(accumulate(nums, max))
        ans = [0] * n
        suf_min = inf
        mx = 0
        for i in range(n - 1, -1, -1):
            if pre_max[i] <= suf_min:
                mx = pre_max[i]
            suf_min = min(suf_min, nums[i])
            ans[i] = mx
        return ans
    
class Solution:
    # 灵神
    # + 动态规划 
    # ans[i] = 1. preMax[i], preMax[i]≤sufMin[i+1]
    #          2. ans[i + 1], preMax[i]>sufMin[i+1]
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = list(accumulate(nums, max))  # nums 的前缀最大值

        ans = [0] * n
        suf_min = inf
        for i in range(n - 1, -1, -1):
            ans[i] = pre_max[i] if pre_max[i] <= suf_min else ans[i + 1]
            suf_min = min(suf_min, nums[i])
        return ans


class Solution:
    # 菲莉斯
    # 并查集
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        parents = list(range(n))
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        mx = nums[:]
        def merge(x, y):
            a, b = find(x), find(y)
            if a != b:
                parents[a] = b
                mx[b] = max(mx[b], mx[a])

        pre_max = list(accumulate(nums, max))
        suf_min = list(accumulate(nums[::-1], min))[::-1]
        for i in range(n - 1):
            if pre_max[i] > suf_min[i + 1]:
                merge(i, i + 1)
        
        return [mx[find(i)] for i in range(n)]
    