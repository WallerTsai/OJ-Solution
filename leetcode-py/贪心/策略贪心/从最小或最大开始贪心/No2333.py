from typing import List
import heapq

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        differs = []
        for l1,l2 in zip(nums1,nums2):
            differs.append(abs(l2-l1))
        differs.sort(reverse=True)

        temp = 0
        for i,differ in enumerate(differs):
            if temp <= k1+k2:
                temp += differ
                continue
            if temp - differ*i <= k1+k1:
                temp += differ
            else:
                res = 0
                a = (temp-k1-k2) % i
                for _ in range(a):
                    res += (differ-1) ** 2
                for _ in range(i-a):
                    res += differ ** 2
                for j in differs[i:]:
                    res += j ** 2
                return res
        return 0    # 错误
                

# class Solution:
#     def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
#         differs = []
#         for l1,l2 in zip(nums1,nums2):
#             differs.append(abs(l2-l1))
#         differs.sort(reverse=True)

#         temp = 0
#         for i,differ in enumerate(differs):

#             if temp <= k1+k2 or (temp - differ*i) <= k1+k2:
#                 temp += differ
#             else:
#                 res = 0
#                 differ_2 = (temp - differ*i) - (k1+k2)
#                 for _ in range(differ_2):
#                     res += (differ+1)**2
#                 for _ in range(i-differ_2):
#                     res += differ ** 2
#                 for j in differs[i:]:
#                     res += j**2
#                 return res
#         return 0 # 错误

# class Solution:
#     def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
#         differs = []
#         for l1,l2 in zip(nums1,nums2):
#             differs.append(abs(l2-l1))
#         differs.sort(reverse=True)

#         res = 0
#         dummy = differs[0]
#         k = k1+k2
#         index = 1
#         while k > 0:
#             for i in range(index,len(differs)):
#                 if differs[i] != dummy:
#                     index = i
#                     break
#                 if i == len(differs):
#                     k = 0
#             if k >= (dummy-differs[index]) * index:
#                 k -= (dummy-differs[index]) * index
#                 dummy = differs[index]
#             else:
#                 a = k // index
#                 differs[:index] = [dummy-a]*index
#                 k -= a * index
#                 break
#         for _ in range(k):
#             res += (dummy-1)**2
#         for j in differs[k:]:
#             res += j ** 2
#         return res  # 错误



class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_heap = [-d for d in diff]  # 用负值模拟最大堆
        heapq.heapify(max_heap)
        
        total_moves = k1 + k2
        
        # 使用操作次数减少差值
        while total_moves > 0 and max_heap:
            max_diff = -heapq.heappop(max_heap)  # 取出当前最大的差值
            if max_diff == 0:  # 如果最大差值已经是 0，就无需操作
                break
            
            max_diff -= 1  # 减少差值
            total_moves -= 1
            heapq.heappush(max_heap, -max_diff)  # 调整后放回堆
        
        # 计算最小差值平方和
        result = 0
        while max_heap:
            diff = -heapq.heappop(max_heap)
            result += diff ** 2
        
        return result # 超时
    
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_moves = k1 + k2
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        # 如果全部可以修改成0
        if total_moves >= sum(diff):
            return 0

        # 差值从大到小排序
        diff.sort(reverse=True)
        diff.append(0)  # 哨兵，用于处理最后的边界情况
        
        # 贪心分配修改次数
        for i in range(n):
            count = (i + 1) * (diff[i] - diff[i + 1])  # 当前差值减少到下一个差值需要的次数
            if total_moves >= count:
                total_moves -= count
            else:
                # 如果剩余的修改次数不足以降到下一层，均匀分配到前 i+1 个差值
                reduce_by = total_moves // (i + 1)
                remainder = total_moves % (i + 1)
                for j in range(i + 1):
                    diff[j] -= reduce_by
                for j in range(remainder):
                    diff[j] -= 1
                break
        
        # 计算最小平方和
        return sum(d ** 2 for d in diff if d > 0)   # 超时

class Solution:
    # gpt-4o
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        from collections import Counter

        n = len(nums1)
        total_moves = k1 + k2  # 总修改次数
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]  # 差值数组

        if total_moves >= sum(diff):
            # 如果修改次数足够多，直接将所有差值归零
            return 0

        # 统计差值频率
        max_diff = max(diff)
        freq = [0] * (max_diff + 1)
        for d in diff:
            freq[d] += 1

        # 从大到小减少差值
        for i in range(max_diff, 0, -1):
            if freq[i] == 0:
                continue  # 当前差值没有出现
            if total_moves >= freq[i]:
                # 可以将这一层全部减少
                freq[i - 1] += freq[i]
                total_moves -= freq[i]
                freq[i] = 0
            else:
                # 修改次数不足，均匀减少这一层
                freq[i - 1] += total_moves
                freq[i] -= total_moves
                total_moves = 0
                break

        # 计算最小平方和
        return sum(f * (i ** 2) for i, f in enumerate(freq) if f > 0) # 98ms

class Solution:
    # leetcode 某个大佬
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        # 如果全部可以修改成0
        if k >= sum(diff):
            return 0

        # 差值从大到小排序
        diff.sort(reverse=True)
        diff.append(0)  # 哨兵，用于处理最后的边界情况

        for i,x in enumerate(diff):
            k -= (diff[i-1] - x) * i # 这里巧妙的避免了i=0越界问题
            if k < 0:
                break
        
        a,b = divmod(-k,i) # 返回(结果,余数)
        res = b * (diff[i] + a + 1)**2 + (i - b) * (diff[i] + a)**2 + sum(x**2 for x in diff[i:])
        # 上面这个数学方法用的非常巧妙
        return res  # 89ms

fun = Solution()
res = fun.minSumSquareDiff([7,11,4,19,11,5,6,1,8],[4,7,6,16,12,9,10,2,10],3,6)
print(res)

