from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # No94
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

    # No108
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def trackback(left, right):
            # [left, right)
            if left == right:
                return None
            mid = (left + right) // 2
            return TreeNode(nums[mid],trackback(left, mid), trackback(mid + 1, right))
        
        return trackback(0, len(nums))
    
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = self.inorderTraversal(root)
        return self.sortedArrayToBST(nums)



class Solution:
    # DSW
    # 作者：wxyz
    # https://leetcode.cn/problems/balance-a-binary-search-tree/solutions/3899414/shuang-jie-zhong-xu-bian-li-gou-zao-bstl-2tsl/
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(-1)
        dummy.right = root

        # 将树拉直成一个只有右子节点的链表
        cnt = 0
        temp = dummy
        while temp.right:
            if temp.right.left:
                # 右旋操作：
                old_node = temp.right
                new_node = old_node.left
                # 连接
                temp.right = new_node
                old_node.left = new_node.right
                new_node.right = old_node
            else:
                cnt += 1
                temp = temp.right
                
        # 这一轮“完美”层级能容纳的节点数
        # bit_length() 返回二进制表示的位数。
        # 公式实际上是求不超过 cnt 的最大的 (2^k - 1)
        m = 2 ** (cnt.bit_length() - 1) - 1  

        def compress(node, times):
            # 对 node 右侧的链表执行 times 次左旋
            temp = node 
            for _ in range(times):
                # 确保有足够的节点进行旋转
                if not temp.right or not temp.right.right:
                    break
                
                # 左旋操作：
                child = temp.right
                pivot = child.right
                # 连接
                child.right = pivot.left
                pivot.left = child
                temp.right = pivot

                # 移动
                temp = pivot

        # 处理多余的节点，将非完全二叉树底层的多余叶子折叠上去
        compress(dummy, cnt - m)

        # 循环压缩，每次对剩下节点的一半进行左旋
        while m > 1:
            m //= 2
            compress(dummy, m)

        return dummy.right