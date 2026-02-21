from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        
        res = list()
        postorder(root)
        return res
    


# 2026年2月9日
class Solution:
    # Morris遍历
    # 在No144稍作修改即可
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            # left -> right, right -> left
            if root.right:
                # 找root的前驱节点(中序遍历中,root的前一个节点)
                pre:TreeNode = root.right
                while pre.left and pre.left is not root:
                    pre = pre.left

                # root的右子树未访问
                if pre.left is None:
                    res.append(root.val)    # 直接添加答案
                    pre.left = root    # 建立线索
                    root = root.right
                    continue

                # root的右子树已访问
                pre.left = None    # 恢复
                root = root.left   
                continue            # 同样跳过

            res.append(root.val)
            root = root.left

        res.reverse()   # 注意
        return res
    

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.right is None:
                ans.append(root.val)
                root = root.left
            else:
                next = root.right
                while next.left and next.left != root:
                    next = next.left
                if next.left != root:
                    ans.append(root.val)
                    next.left = root
                    root = root.right
                else:
                    next.left = None
                    root = root.left
        return ans[::-1]

