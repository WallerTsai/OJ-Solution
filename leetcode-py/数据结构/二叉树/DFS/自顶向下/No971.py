# Definition for a binary tree node.


from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        dq = deque(voyage)
        stack = [root]

        if root.val != dq.popleft():
            return [-1]
        
        ans = []
        while stack:
            root = stack.pop()
            if root is None:
                continue
            t = dq.popleft()
            if root.left and root.left.val == t:
                stack.append(root.right)
                stack.append(root.left)
            elif root.right and root.right.val == t:
                ans.append(root.val)
                stack.append(root.left)
                stack.append(root.right)

        return ans if not dq else [-1]  # 错误
    

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        dq = deque(voyage)
        stack = [root]
        
        ans = []
        while stack:
            node = stack.pop()
            if node is None:
                continue

            if node.val != dq[0]:
                return [-1]
            
            dq.popleft()

            if node.left and node.left.val != dq[0]:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                stack.append(node.right)
                stack.append(node.left)

        return ans
    

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        ans = []
        idx = 0
        flag = True
        def dfs(node: Optional[TreeNode]):
            nonlocal flag, idx
            if not flag or node is None:
                return
            
            if node.val != voyage[idx]:
                flag = False
                return
            
            idx += 1

            if node.left and node.left.val != voyage[idx]:
                ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ans if flag else [-1]


