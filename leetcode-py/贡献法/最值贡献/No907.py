from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr = [-1] + arr + [-1]
        st = []
        ans = 0
        for right, x in enumerate(arr):
            while st and arr[st[-1]] > x:
                cur_idx = st.pop()
                cur_val = arr[cur_idx]

                left = st[-1]
                # 计算贡献
                count = (cur_idx - left) * (right - cur_idx)
                ans = (ans + cur_val * count) % MOD

            st.append(right)
        return ans



