from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    # BFS
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_sum = -inf
        level = 1
        q = [root]
        while q:
            temp = q
            q = []
            total = 0
            for node in temp:
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if total > max_sum:
                max_sum = total
                ans = level
            
            level += 1

        return ans
    


class Solution:
    # DFS
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

            if len(row_sum) == level:  # 首次访问 level 层
                row_sum.append(node.val)  # 节点值作为层和的初始值
            else:
                row_sum[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        row_sum = []
        dfs(root, 0)
        return row_sum.index(max(row_sum)) + 1  # 层号从 1 开始