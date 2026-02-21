# Definition for a binary tree node.

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root.left and root.right:
                return 1 + min(dfs(root.left), dfs(root.right))
            elif root.left:
                return 1 + dfs(root.left)
            elif root.right:
                return 1 + dfs(root.right)
            return 1
        return dfs(root)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = inf
        def dfs(node: Optional[TreeNode], cnt: int) -> None:
            if node is None:
                return
            cnt += 1
            if node.left is node.right:  # node 是叶子
                nonlocal ans
                ans = min(ans, cnt)
                return
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        dfs(root, 0)
        return ans if root else 0