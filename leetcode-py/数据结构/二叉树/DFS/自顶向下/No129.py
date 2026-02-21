from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode],count):
            if not root:
                return 
            count = count * 10 + root.val
            if root.left is root.right:
                nonlocal ans
                ans += count
            dfs(root.left,count)
            dfs(root.right,count)
        dfs(root,0)
        return ans