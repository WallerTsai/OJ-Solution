from collections import defaultdict
from typing import List

# 1.首先分析题目：如果所有数的每一列二进制位上的1的个数是偶数，则可以把这一位变成0，否则不行
#   这就需要我们使用异或操作
# 2.异或的性质 !类似! 于加法(前缀和)，可以参考lc560的解法:哈希表+前缀和
    # 为什么说异或的性质类似于加法
    # 首先了解一下异或的性质:
    # 1.任何数与本身异或都等于0
    # 2.任何数与0异或都等于本身
    # 例:  a4 ^ a5 = (a1 ^ a2 ^ a3 ^ a4 ^ a5) ^ (a1 ^ a2 ^ a3)
    # 则 当 (a1 ^ a2 ^ a3 ^ a4 ^ a5) = (a1 ^ a2 ^ a3),那么 a4 ^ a5 = 0
    # 对应lc560前缀和 s5 - s3 = k -> s5 - k = s3 这里 k = 0
    # 当统计到s5 时候,查询哈希表[s5 - k],其值在遍历s3时候存取
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s ^= x
            ans += cnt[s]
            cnt[s] += 1
        return ans 
    
# 总结: s = s[j] ^ s[i] (j>i)