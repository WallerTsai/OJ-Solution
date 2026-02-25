from math import inf
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 前序遍历
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder_check(root: Optional[TreeNode], left = -inf, right = inf):
            if root is None:
                return True
            return left < root.val < right and preorder_check(root.left, left, root.val) and preorder_check(root.right, root.val, right)
        return preorder_check(root)


class Solution:
    # 中序遍历
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_check(root: Optional[TreeNode]):
            if root is None:
                return True
            if not inorder_check(root.left):
                return False
            if root.val <= self.pre:
                return False
            self.pre = root.val
            return inorder_check(root.right)
        return inorder_check(root)


class Solution:
    # 灵神
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf



