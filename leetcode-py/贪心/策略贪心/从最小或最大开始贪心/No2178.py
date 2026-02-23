# 难度中等
from typing import List

# class Solution:
#     def maximumEvenSplit(self, finalSum: int) -> List[int]:
#         if finalSum % 2 != 0:
#             return []
#         res = []
#         path = []
#         def dfs(sum,next):
#             nonlocal res
#             flat = False
#             for i in range(next,finalSum+1,2):
#                 path.append(i)
#                 sum += i

#                 if sum == finalSum:
#                     if len(res) < len(path):
#                         res = path[:]
#                     flat = True
#                 elif sum > finalSum:
#                     flat = True
#                 else:
#                     dfs(sum,next+2)

#                 sum -= i
#                 path.pop()
#                 if flat:
#                     return
#         dfs(0,2)
#         return res  # 超时，超级超级慢
    
# from typing import List

class Solution:
    # 不应该使用递归
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        
        res = []
        path = []
        
        def dfs(sum, next):
            nonlocal res
            # 如果当前路径的和等于finalSum，且当前路径长度大于结果路径长度，则更新结果路径
            if sum == finalSum:
                if len(res) < len(path):
                    res = path[:]
                return  False
            # 如果当前路径的和超过finalSum，或者next超过了finalSum，则返回
            if sum > finalSum or next > finalSum:
                return  False
            # 尝试添加下一个偶数到路径中
            for i in range(next, finalSum + 1, 2):
                    path.append(i)
                    flat = dfs(sum + i, i + 2)  # 递归使用下一个更大的偶数
                    path.pop()
                    if not flat:
                        break
            return True
        # 从0开始，下一个偶数是2
        dfs(0, 2)
        return res

# class Solution:
#     def maximumEvenSplit(self, finalSum: int) -> List[int]:
#         if finalSum % 2:
#             return []
#         ans = []
#         i = 2
#         while i <= finalSum:
#             ans.append(i)
#             finalSum -= i
#             i += 2
#         ans[-1] += finalSum
#         return ans

# # 作者：灵茶山艾府
# # 链接：https://leetcode.cn/problems/maximum-split-of-positive-even-integers/solutions/1277705/tan-xin-jian-ji-xie-fa-by-endlesscheng-uxbg/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


fun = Solution()
outcome = fun.maximumEvenSplit(200)
print(outcome)