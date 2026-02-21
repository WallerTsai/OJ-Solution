from typing import Optional

# 暴力可以做，但是要充分利用好完全二叉树的性质
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 暴力递归
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return dfs(node.left) + dfs(node.right) + 1
        
        return dfs(root)
    

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        h = 0
        while root:
            root = root.left
            h += 1

        return h

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 求左右子树的高度
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # 分类讨论
        if left_height == right_height:
            return (2 ** left_height - 1) + self.countNodes(root.right) + 1
        else:
            return (2 ** right_height - 1) + self.countNodes(root.left) + 1
        

class Solution:
    # 大佬版
    # 二分查找 + 位运算
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def check() -> bool:
            node = root
            bit = 1 << (level - 2)     # 初始化开始匹配的位
            while bit > 0:
                # 将节点编号的二进制看成从根节点到节点的路径编码，根据节点编号寻找节点
                if (bit & mid) == 0:
                    node = node.left
                else:
                    node = node.right
                bit >>= 1

            return node is not None    # 节点不为空，说明编号为id的节点存在

        # 统计二叉树层数 
        node = root
        level = 0
        while node:
            level += 1
            node = node.left
        if level <= 1: return level # 层数小于等于1，直接返回节点个数
        # 二分查找节点个数，左闭右开[left, right)
        left = 1 << (level - 1)    # 左边界为最少个数
        right = 1 << level         # 右边界为最多个数+1
        ans = left     # 最终结果
        while left < right:
            mid = left + ((right - left) >> 1)
            if check():    
                # 第mid个节点存在，说明最终结果一定大于等于mid，暂存mid并更新左边界以寻找编号更大的节点是否存在
                ans = mid
                left = mid + 1
            else:
                # 第mid个节点不存在，说明结果小于mid，更新右边界查找编号更小的节点是否存在
                right = mid
        return ans
    
