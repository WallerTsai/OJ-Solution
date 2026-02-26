from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        def dfs(i: int):
            res = [i]
            a_set.add(i)
            j = nums[i]
            while j not in a_set:
                a_set.add(j)
                res.append(j)
                j = nums[j]
            return res
            
        a_set = set()
        n = len(nums)
        need = []
        for i in range(n):
            if i not in a_set and nums[i] != i:
                need.append(dfs(i))

        ans = {range(n)}
        for res in need:
            n_set = set()
            for i in range(1, len(res)):
                temp = res[i] & res[0]
                check = 1
                for j in range(1, len(res)):
                    if j != i and (res[j] & res[i]) != temp:
                        check = 0
                        break
                if check:
                    n_set.add(i)
            
            ans &= n_set

        return max(ans)
    
# 这题不应该是 先按照连通分量来寻找共同的 k 
# 假设答案为 k，那么所有满足 i AND k == k 的下标 i 都能以下标 k 为中继点进行任意交换，
# 而剩下的下标都无法改变元素。这也告诉我们，k=0 至少是可行解。
# 只有 nums[i] != i 的下标 i 才需要改变元素，
# 所以答案就是所有这些下标 AND 起来的结果。复杂度 O(n)。

# 例 [0,2,3,1] 
# 1, 2, 3 两两间按位与，各不同
# 但是可以通过 0 作为中介回到各自位置

class Solution:
    # 脑筋急转弯
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums[i] == i for i in range(n)):
            return 0
        res = (1 << 20) - 1
        for i in range(n):
            if nums[i] != i:
                res &= i
        return res
    
fun = Solution()
fun.sortPermutation([0,2,3,1])