# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(listnode: Optional[ListNode], treenode: Optional[TreeNode]) -> bool:
            if listnode is None:
                return True
            if treenode is None:
                return False
            if listnode.val == treenode.val:
                return dfs(listnode.next, treenode.left) or dfs(listnode.next, treenode.right)
            elif not (listnode is head):
                return False
            if listnode is head:
                return dfs(listnode, treenode.left) or dfs(listnode, treenode.right)

        return dfs(head, root)  # 错误


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(listnode: Optional[ListNode], treenode: Optional[TreeNode]) -> bool:
            if listnode is None:
                return True
            if treenode is None:
                return False
            
            if listnode.val == treenode.val and (dfs(listnode.next, treenode.left) or dfs(listnode.next, treenode.right)):
                return True
            elif  listnode is head and  (dfs(listnode, treenode.left) or dfs(listnode, treenode.right)):
                return True
            else:
                return False

        return dfs(head, root)  # 0ms
    

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(listnode: Optional[ListNode], treenode: Optional[TreeNode]) -> bool:
            if listnode is None:
                return True
            if treenode is None:
                return False
            if listnode.val != treenode.val:
                return False
            return match(listnode.next, treenode.left) or match(listnode.next, treenode.right)
        
        def dfs(treenode: Optional[TreeNode]) -> bool:
            if treenode is None:
                return False
            return match(head, treenode) or dfs(treenode.left) or dfs(treenode.right)
        
        return dfs(root)    # 3ms