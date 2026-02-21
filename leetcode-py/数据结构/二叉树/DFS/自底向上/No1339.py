from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

fmax = lambda x, y : x if x > y else y
MOD = 1_000_000_007
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs1(node):
            if node is None:
                return 0
            return node.val + dfs1(node.left) + dfs1(node.right)
        
        total = dfs1(root)

        def dfs2(node): 
            if node is None:
                return 0
            
            s = node.val + dfs2(node.left) + dfs2(node.right)
            nonlocal ans
            ans = fmax(ans, s * (total - s))
            return s
        
        ans = 0
        dfs2(root)
        return ans % MOD
    

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub_sum.append(s)
            return s

        sub_sum = []
        total = dfs(root)

        ans = max(s * (total - s) for s in sub_sum)
        return ans % 1_000_000_007