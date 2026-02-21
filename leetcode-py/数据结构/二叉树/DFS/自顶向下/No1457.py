# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt = [0] * 10

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            cnt[root.val] ^= 1
            if root.left is root.right:
                res = 1 if sum(cnt) <= 1 else 0
            else:
                res = dfs(root.left) + dfs(root.right)
            cnt[root.val] ^= 1 # 恢复现场
            return res
        
        return dfs(root)


class Solution:
    # 灵神
    def pseudoPalindromicPaths(self, root: Optional[TreeNode], mask=0) -> int:
        if root is None:
            return 0
        mask ^= 1 << root.val  # 修改 root.val 出现次数的奇偶性
        if root.left is root.right:  # root 是叶子节点
            return 1 if mask & (mask - 1) == 0 else 0
        return self.pseudoPalindromicPaths(root.left, mask) + \
               self.pseudoPalindromicPaths(root.right, mask)
