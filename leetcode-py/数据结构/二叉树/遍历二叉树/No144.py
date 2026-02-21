from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        res = list()
        preorder(root)
        return res

class Solution:
    # Morris 遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res
        
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right
        
        return res
    

# 2026年2月9日
class Solution:
    # 在No94稍作修改即可
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:
                # 找root的前驱节点(中序遍历中,root的前一个节点)
                pre:TreeNode = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right

                # root的左子树未访问
                if pre.right is None:
                    res.append(root.val)    # 不同点1：直接添加答案
                    pre.right = root    # 建立线索
                    root = root.left
                    continue

                # root的左子树已访问
                pre.right = None    # 恢复
                root = root.right   # 不同点2：已经访问到root的前线索节点则跳过，访问root的右节点
                continue            # 不同点3

            res.append(root.val)
            root = root.right

        return res
    

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    ans.append(root.val)
                    prev.right = root
                    root = root.left
                else:
                    prev.right = None
                    root = root.right
        return ans



