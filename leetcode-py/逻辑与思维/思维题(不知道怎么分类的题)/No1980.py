from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        _set = set(nums)
        for i in range(1 << n - 1, 1 << n):
            if str(bin(i)[2:]) not in _set:
                return str(bin(i)[2:])
        return '0' * n
    

class Solution:
    # 康托对角线
    # https://leetcode.cn/problems/find-unique-binary-string/solutions/951165/go-jian-ji-xie-fa-by-endlesscheng-mcwc/
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = [''] * len(nums)
        for i, s in enumerate(nums):
            ans[i] = '1' if s[i] == '0' else '0'
        return ''.join(ans)