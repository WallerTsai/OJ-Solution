from typing import Optional, Tuple


# Definition for a binary tree node.
fmax = lambda x, y : x if x > y else y
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1

        def dfs(node: Optional[TreeNode], depth: int):
            nonlocal ans, max_depth

            if node is None:
                max_depth = fmax(max_depth, depth)
                return depth
            
            left_max_depth = dfs(node.left, depth + 1)
            right_max_depth = dfs(node.right, depth + 1)

            if left_max_depth == right_max_depth == max_depth:
                ans = node

            return fmax(left_max_depth, right_max_depth)

        dfs(root, 0)

        return ans
    

class Solution:
    # 自底向上
    # 灵神
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if node is None:
                return 0, None

            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            if left_height > right_height:  # 左子树更高
                return left_height + 1, left_lca
            if left_height < right_height:  # 右子树更高
                return right_height + 1, right_lca
            return left_height + 1, node  # 一样高

        return dfs(root)[1]


