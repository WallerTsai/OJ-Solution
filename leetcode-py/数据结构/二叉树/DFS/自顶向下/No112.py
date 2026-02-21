from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = False
        def dfs(root: Optional[TreeNode], count):
            if not root:
                return 
            count += root.val
            if root.left is root.right:
                if count == targetSum:
                    nonlocal flag
                    flag = True
            dfs(root.left,count)
            dfs(root.right,count)
        dfs(root,0)
        return flag




