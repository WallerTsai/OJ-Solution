from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        # 先计算左边界
        left,stack = [-1] * n, []
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] >= x:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # 再计算右边界
        right,stack = [n] * n, []
        for i in range(n - 1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i ,(x,l,r) in enumerate(zip(arr,left,right)):
            ans += x * (i-l) * (r-i)
        
        return ans % (10 ** 9 + 7)

