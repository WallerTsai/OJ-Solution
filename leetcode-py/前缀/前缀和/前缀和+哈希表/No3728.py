from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        cnt = defaultdict(list)
        ans = pre_sum = 0
        for i, num in enumerate(capacity):
            for x, j in cnt[num]:
                if i - j < 2:
                    continue
                if pre_sum - x == num:
                    ans += 1
            pre_sum += num
            cnt[num].append((pre_sum, i))
        return ans  # 超时
    

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        cnt = defaultdict(dict)
        ans = pre_sum = 0
        for i, num in enumerate(capacity):
            ans += cnt[num].get(pre_sum - num, 0)
            if i and num == capacity[i - 1] == 0:
                ans -= 1
            pre_sum += num
            cnt[num][pre_sum] = cnt[num].get(pre_sum, 0) + 1
        return ans  # 312ms
    

# capacity[l] = capacity[r] = s[r - 1] − s[l]
# -->
# capacity[l] = capacity[r]
# capacity[l] + s[l] = s[r - 1]
# 上面只是个人理解，但是不严谨

# 根据前缀和的定义: s[0] = 0  s[n] = nums[0] + nums[1] + ... + nums[n - 1]
# 所以 capacity[l] = capacity[r] = s[r] − s[l + 1]


# 为保证 r−l+1≥3，可以在枚举 r 的同时，先查询哈希表更新答案，
# 再把二元组 (capacity[r−1],capacity[r−1]+s[r - 1]) 加到哈希表，
# 这样对于下一轮循环的 r+1 来说，把添加的 r−1 作为 l，
# 与 r+1 构成的子数组长度就是 (r+1)−(r−1)+1=3，满足要求。
class Solution:
    # 灵神
    def countStableSubarrays(self, capacity: List[int]) -> int:
        cnt = defaultdict(int)
        s = capacity[0]  # 前缀和
        ans = 0
        for last, x in pairwise(capacity):
            print(x)
            ans += cnt[(x, s)]
            cnt[(last, last + s)] += 1
            s += x
        return ans  # 702ms
