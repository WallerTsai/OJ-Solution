from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode],val: int):
            if not root:
                return
            if root.val >= val:
                nonlocal ans
                ans += 1
                val = root.val
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,-10_001)

        return ans



