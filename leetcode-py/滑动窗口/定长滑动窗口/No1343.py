from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arr.sort(reverse=True)
        cur_sum = sum(arr[:k])

        if cur_sum < threshold * k:
            return 0
        res = 1
        for i in range(k,len(arr)):
            if arr[i] == arr[i-k]:
                continue
            else:
                cur_sum  = cur_sum + arr[i] - arr[i-k]
            if cur_sum >= threshold * k:
                res += 1
            else:
                break
        return res
    # 思路没问题，只是题目中的“子数组”是连续的(存在异议)

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        cur_sum = sum(arr[:k])
        res = 1 if cur_sum >= threshold * k else 0
        for i in range(k,len(arr)):
            cur_sum  = cur_sum + arr[i] - arr[i-k]
            if cur_sum >= threshold * k:
                res += 1
        return res  # 31ms
    
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        cur_sum = sum(arr[:k])
        res = 1 if cur_sum >= target else 0
        for i in range(k,len(arr)):
            cur_sum  = cur_sum + arr[i] - arr[i-k]
            if cur_sum >= target:
                res += 1
        return res  #27ms
    
fun = Solution()
outcome = fun.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5)
print(outcome)