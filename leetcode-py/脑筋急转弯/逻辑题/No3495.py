from functools import cache
from typing import List

# 灵神

# 返回 [1,n] 的单个元素的操作次数之和
def f(n: int) -> int:
    m = n.bit_length()
    res = sum((i + 1) // 2 << (i - 1) for i in range(1, m))
    return res + (m + 1) // 2 * (n + 1 - (1 << m >> 1))

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        return sum((f(r) - f(l - 1) + 1) // 2 for l, r in queries)
    

# mipha大佬

# 预处理范围
arr = [(0,0)]
while arr[-1][-1] <= int(1e9):
    x,y = arr[-1]
    x = y + 1
    y = x * 4 - 1
    arr.append((x,y))

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        print(len(arr))
        '''
        queries[i] = l,r
        数组为 range(l,r+1)
        l < r
        1 1 1 2 2
        1 + 1 + 1 + 1

        预处理出范围
        0,0    0
        1,3    1
        4,15   2
        16 63  3
        64,255 4
        
        '''
        res = 0
        for l,r in queries:
            # 找起点
            i = 0
            while i < len(arr):
                if arr[i][0] <= l <= arr[i][1]:
                    break
                i += 1
            # 移除左侧
            t = -(l-arr[i][0])*i
            x,y = arr[i]
            while y <= r:
                t += (y - x + 1) * i
                i += 1
                x,y = arr[i]
            # 补齐右侧
            t += (r - arr[i][0] + 1) * i
            res += (t+1)//2

        return res
    

class Solution:
    # 前缀和
    def minOperations(self, queries: List[List[int]]) -> int:
        def cal_prefix(x: int):
            res = 0
            l = r = 0
            times = 1
            while r <= x:
                l = r + 1
                r = l * 4 - 1
                length = min(r, x) - l + 1
                res += times * length
                times += 1
            print(res)
            return res
        
        ans = 0
        for l, r in queries:
            total = cal_prefix(r) - cal_prefix(l - 1)
            ans += (total + 1) // 2 # 向上取整

        return ans  # 2299ms


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        @cache
        def cal_prefix(x: int):
            res = 0
            l = r = 0
            times = 1
            while r <= x:
                l = r + 1
                r = l * 4 - 1
                length = min(r, x) - l + 1
                res += times * length
                times += 1
            print(res)
            return res
        
        ans = 0
        for l, r in queries:
            total = cal_prefix(r) - cal_prefix(l - 1)
            ans += (total + 1) // 2 # 向上取整

        return ans  # 2553ms





# 预处理
prefix = [0]
for x in range(1, 10 ** 9 + 1):
    prefix.append(prefix[-1] + x // 4 + 1)


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            total = prefix[r] - prefix[l - 1]
            ans += (total + 1) // 2 # 向上取整

        return ans  #炸内存

# 灵神代码解析
def f(x: int):
    m = x.bit_length()
    res = 0
    for i in range(1, m):
        t = (i + 1) // 2    # 该段变成 0 需要的次数
        l = 1 << (i - 1)    # 该段长度
        res += t * l

    rm_t = (m + 1) // 2
    # rm_l = x + 1 - (1 << (m - 1))   # ValueError: negative shift count   当 m 为 0
    rm_l = x + 1 - (1 << m >> 1)

    return res + rm_t * rm_l

    
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        return sum((f(r) - f(l - 1) + 1) // 2 for l, r in queries)  # 2259


# leetcode 大佬
ACC = [0] * 32  # 前缀和数组
for bit_len in range(1, 32):
    # 该位长的元素个数
    cnt = 1 << (bit_len - 1)
    # 该位长的元素变成0需要的次数
    x = (bit_len+1) // 2
    ACC[bit_len] = ACC[bit_len-1] + cnt * x  # 累加总位长

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # 整除4等于右移2次，一直除到0等于右移位长次
        # 假设x的位长为n，那么x需要(n+1) // 2次整除4才能变为0

        # 虽然把一个数组的元素全变成0的操作次数，需要看数组中最大的数字的位长max_len
        # 实际操作次数 = max((total_len + 1) // 2, max_len)
        # 但对于题目中的这样一个连续数组，最大的数字的位长，不会超过剩余数字位长之和+1
        # 我们可以直接统计数组中所有元素的位长之和total_len
        # (total_len+1) // 2就是把它们全部变成0需要的操作次数
        
        # 那么下一个问题，就是把[l, r]按照位长进行分段，计算每个位长值对应的数字有多少个
        # 比如[6, 34]，就要分成[6, 7], [8, 15], [16, 31], [32, 34]四段
        # 对应的位长分别为3, 4, 5, 6
        ans = 0
        for i, (l, r) in enumerate(queries):
            min_len = l.bit_length()
            max_len = r.bit_length()
            if min_len == max_len:  # 只有这一段
                x = (min_len + 1) // 2
                ans += (x * (r-l+1) + 1) // 2
                continue
            
            # 找到min_len这个位长的元素个数
            total = 0
            cnt = (1 << min_len) - l
            total += cnt * ((min_len + 1) // 2)

            # 找到max_len这个位长的元素个数
            cnt = r - (1 << (max_len-1)) + 1
            total += cnt * ((max_len + 1) // 2)

            # 找到中间位长的个数，这里查询预处理结果了
            total += ACC[max_len-1] - ACC[min_len]

            ans += (total + 1) // 2  # 把位长之和变成操作数
        return ans



fun = Solution()
fun.minOperations([[1,2],[2,4]])