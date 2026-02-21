from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            else:
                inorder(root=root.left)
                res.append(root.val)
                inorder(root=root.right)

        inorder(root)

        return res


# 2026年2月9日      
# Morris遍历
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:
                # 找root的前驱节点(中序遍历中,root的前一个节点)
                pre:TreeNode = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right

                # root的左子树未访问
                if pre.right is None:
                    pre.right = root    # 建立线索
                    root = root.left
                    continue

                # root的左子树已访问
                pre.right = None    # 恢复
            
            res.append(root.val)
            root = root.right

        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.left is None:
                ans.append(root.val)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right is None:
                    prev.right = root
                    root = root.left
                else:
                    ans.append(root.val)
                    prev.right = None
                    root = root.right
        return ans