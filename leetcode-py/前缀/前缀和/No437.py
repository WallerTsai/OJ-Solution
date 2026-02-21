# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(node: TreeNode, cnt: dict, cur: int):
            if node is None:
                return
            cur = (cur + node.val) % targetSum
            nonlocal ans
            if cnt[cur]:
                print(node.val)
            ans += cnt[cur]
            cnt[cur] += 1
            new_cnt1 = cnt.copy()
            new_cnt2 = cnt.copy()
            dfs(node.left, new_cnt1, cur)
            dfs(node.right, new_cnt2, cur)
        
        cnt = defaultdict(int)
        cnt[0] = 1
        dfs(root,cnt,0)
        return ans  # 题目要求是等于targetSum 不是包括倍数
    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        def dfs(node: TreeNode, cnt: dict, cur: int):
            if node is None:
                return
            cur += node.val
            nonlocal ans
            ans += cnt[cur - targetSum]
            cnt[cur] += 1
            new_cnt1 = cnt.copy()
            new_cnt2 = cnt.copy()
            dfs(node.left, new_cnt1, cur)
            dfs(node.right, new_cnt2, cur)
        
        cnt = defaultdict(int)
        cnt[0] = 1
        dfs(root,cnt,0)
        return ans  # 内存大
    
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1

        def dfs(node: Optional[TreeNode], s: int) -> None:
            if node is None:
                return
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1  # 恢复现场

        dfs(root, 0)
        return ans