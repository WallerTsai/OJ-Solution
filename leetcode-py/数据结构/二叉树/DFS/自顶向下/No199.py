from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        map = defaultdict(int)
        def dfs(root: Optional[TreeNode],depth):
            if not root:
                return
            nonlocal map
            map[depth] = root.val
            dfs(root.left,depth + 1)
            dfs(root.right,depth + 1)
        dfs(root,0)
        ans = []
        for i,v in map.items():
            ans.append(v)
        return ans


