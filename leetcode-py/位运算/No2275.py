from functools import cache
from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        length = len(candidates)
        
        @cache
        def dfs(i,num,count):

            if num > 0 or count == 0:
                nonlocal res
                res = max(res,count)
            else:
                return
            
            for x in range(i,length):
                if num == 0:
                    dfs(x+1,candidates[x],count+1)
                else:
                    dfs(x+1,(num & candidates[x]),count+1)
                
        dfs(0,0,0)
        return res  # 超时

class Solution:
    # 时间复杂度：O(n⋅k)，其中 n 是数组 candidates 的长度，k 是数组中最大元素的位数
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0] * max(candidates).bit_length()
        for num in candidates:
            index = 0
            while num:
                cnt[index] += (num & 1)
                num >>= 1
                index += 1
        return max(cnt) # 570ms

class Solution:
    # 逐位检查
    # 时间复杂度：O(n⋅log(mx))其中 n 是数组 candidates 的长度，log(mx) 是最大元素的位数。
    def largestCombination(self, candidates: List[int]) -> int:
        i, mx, ans = 1, max(candidates), 0
        while i <= mx:
            cnt = 0
            for candi in candidates:
                if i & candi > 0:
                    cnt += 1
            ans = max(ans, cnt)
            i <<= 1
        return ans  # 比上面快一半 ：第一种方法更新数组需要一定的时间开销，第二种操作高效

fun = Solution()
print(fun.largestCombination([16,17,71,62,12,24,14]))
