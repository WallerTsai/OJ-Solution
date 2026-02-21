from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #递归原数组下标比递归数组长度简单
        def make_BiTree(start_index:int,end_index:int):

            if start_index>end_index:
                return None

            mid_index = (end_index + start_index)//2    #这里的+注意一下
            root = TreeNode(nums[mid_index])

            root.left = make_BiTree(start_index,mid_index-1)
            root.right = make_BiTree(mid_index+1,end_index)

            return root

        res = make_BiTree(0,len(nums)-1)
        return res


# 2026年2月9日
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def trackback(left, right):
            # [left, right)
            if left == right:
                return None
            mid = (left + right) // 2
            return TreeNode(nums[mid],trackback(left, mid), trackback(mid + 1, right))
        
        return trackback(0, len(nums))