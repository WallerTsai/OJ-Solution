from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], pre_dir, length):
            if not node:
                return
            
            nonlocal ans
            if length > ans:
                ans = length

            dfs(node.left, 0, 1 if not pre_dir else length + 1)
            dfs(node.right, 1, 1 if pre_dir else length + 1)

        dfs(root, 0, 0)
        return ans



