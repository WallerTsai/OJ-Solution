from bisect import bisect_left
from collections import Counter
from math import factorial
from typing import List

# MOD = 1_000_000_007
# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         ans = 0
#         cnt = Counter(arr)
#         key_l = sorted(cnt.keys())
#         n = len(key_l)
#         for i in range(n-1,-1,-1):
#             k = key_l[i]
#             if k * 3 < target:
#                 break
#             # 取三个
#             if cnt[k] >= 3 and k * 3 == target:
#                 ans == (ans + factorial(cnt[k]) // 36) % MOD
#                 continue
#             # 取两个
#             if cnt[k] >= 2:
#                 index = bisect_left(key_l,target - k * 2)
#                 if key_l[index] + k * 2 == target:
#                     ans = (ans + cnt[key_l[index]] * (factorial(cnt[k]) // 4)) % MOD
#             # 取一个
#             if i >= 2:
#                 next_target = target - k
#                 left,right = 0,i-1
#                 while left < right:
#                     l,r = key_l[left],key_l[right]
#                     if l + r == next_target:
#                         ans  = (ans + cnt[l] * cnt[r] * cnt[k]) % MOD
#                         left += 1
#                         right -= 1
#                     elif l + r < next_target:
#                         left += 1
#                     else:
#                         right -= 1
#                 if key_l[right] * 2 == next_target:
#                     ans = (ans + (factorial(cnt[key_l[right]]) // 4) * cnt[k]) % MOD
#         return ans # [1,1,2,2,2,2] 错误，最后只有两个数可以选

MOD = 1_000_000_007
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        cnt = Counter(arr)
        key_l = sorted(cnt.keys())
        n = len(key_l)
        for i in range(n-1,-1,-1):
            k = key_l[i]
            if k * 3 < target:
                break
            # 取三个
            if cnt[k] >= 3 and k * 3 == target:
                ans = (ans + (cnt[k] * (cnt[k]-1) * (cnt[k]-2) // 6)) % MOD
                continue
            # 取两个
            if cnt[k] >= 2:
                index = bisect_left(key_l,target - k * 2)
                if key_l[index] != k and key_l[index] + k * 2 == target:
                    ans = (ans + cnt[key_l[index]] * (cnt[k] * (cnt[k]-1) // 2)) % MOD
            # 取一个
            if i >= 1:
                next_target = target - k
                left,right = 0,i-1
                while left < right:
                    l,r = key_l[left],key_l[right]
                    if l + r == next_target:
                        ans  = (ans + cnt[l] * cnt[r] * cnt[k]) % MOD
                        left += 1
                        right -= 1
                    elif l + r < next_target:
                        left += 1
                    else:
                        right -= 1
                if key_l[right] * 2 == next_target:
                    ans = (ans + (cnt[key_l[right]] * (cnt[key_l[right]]-1)//2) * cnt[k]) % MOD
        return ans # 8ms

# 要复习组合问题了



if __name__ == "__main__":
    fun  = Solution()
    arr = [3,3,0,0,3,2,2,3]
    print(fun.threeSumMulti(arr,6))