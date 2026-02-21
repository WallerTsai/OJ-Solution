from typing import List
# class Solution:
#     # 递归
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         path = []
#         length = len(s)

#         def backtrack(i:int):
#             if i == length:
#                 res.append(path[:])             # 全局变量用深度拷贝添加到别的列表
#                 return
#             else:
#                 for j in range(i,length):
#                     letter = s[i:j+1]
#                     if letter == letter[::-1]:  # 判断是不是回文
#                         path.append(letter)
#                         backtrack(j+1)          # j前面的字符已经记录了,应该向j而不是i后面递归
#                         path.pop()
#         backtrack(0)
        
#         return res

class Solution:
    # 动态规划
    # 来自leetcode某位不知名的大佬
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]  # 初始化dp数组，dp[i]表示s[:i]所有可能的分割方案
        
        # 遍历字符串s的每个字符
        for i in range(1, len(s) + 1):
            dp.append([])  # 为s[:i]的分割方案初始化一个空列表
            for j in range(i):  # 遍历s[:i]的每个可能的分割点j
                tmp = s[j:i]  # 获取从j到i-1的子串
                if tmp == tmp[::-1]:  # 如果这个子串是回文串
                    # 对于dp[j]中的每个分割方案l，生成一个新的分割方案l + [tmp]
                    # 并将这些新分割方案添加到dp[-1]中
                    for l in dp[j]:  # 遍历dp[j]中的每个分割方案l
                        dp[-1].append(l + [tmp])  # 将l + [tmp]添加到dp[-1]中
        return dp[-1]  # 返回s[:]的所有可能的分割方案

# 注意：List类型需要从typing模块导入

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)

        def dfs(i:int):
            if i == n:
                res.append(path[:])
                return
            else:
                for j in range(i,n):
                    letter = s[i:j+1]
                    if letter == letter[::-1]:
                        path.append(letter)
                        dfs(j+1)
                        path.pop()
        dfs(0)
        return res

class Solution:
    # 递推
    # leetcode 大佬
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]
        # dp[i]表示s[:i]所有可能的分割方案
        for i in range(1, len(s) + 1):
            dp.append([])
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[-1].extend(l + [tmp] for l in dp[j])
        return dp[-1]

if __name__ == "__main__":
    fun = Solution()
    s = "aab"
    out_come = fun.partition(s)
    print(out_come)

