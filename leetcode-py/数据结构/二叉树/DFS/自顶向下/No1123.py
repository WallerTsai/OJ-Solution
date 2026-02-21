# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], fa: Optional[TreeNode], depth: int):
            if node is None: return

            if node.left is None and node.right is None:
                nonlocal g_depth
                if depth > g_depth:
                    nonlocal MAX
                    MAX = fa
                    g_depth = depth

            dfs(node.right,fa=node,depth = depth + 1)
            dfs(node.left,fa=node,depth = depth + 1)

        g_depth = 0
        MAX = TreeNode(val=-1)

        dfs(root.left,root,1)
        dfs(root.right,root,1)

        return MAX  # 审题错误
    
class Solution:
    # 灵神
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1  # 全局最大深度
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 获取左子树最深叶节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 获取右子树最深叶节点的深度
            if left_max_depth == right_max_depth == max_depth:
                ans = node
            return max(left_max_depth, right_max_depth)  # 当前子树最深叶节点的深度
        dfs(root, 0)
        return ans