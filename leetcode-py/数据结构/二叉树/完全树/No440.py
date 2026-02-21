class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        times = 0

        def dfs(i: int):
            nonlocal times
            if times == k:
                return i
            if i <= n:
                i *= 10
                if i <= n:
                    for j in range(10):
                        nex = i + j
                        if nex > n:
                            break
                        times += 1
                        ans = dfs(nex)
                        if ans:
                            return ans
            return 0

        for i in range(1, 10):
            times += 1
            res = dfs(i)
            if res:
                return res

        return 1    # 超时
    

# 十叉树
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # 统计以这为根节点的树的节点的个数
        def count(fa: int) -> int:
            nums = 0
            son = fa + 1
            while fa <= n:
                nums += min(n + 1, son) - fa
                fa *= 10
                son *= 10
            return nums
        
        cur = 1
        k -= 1
        while k > 0:
            steps = count(cur)
            if steps <= k:
                # 不在这棵树上
                cur += 1
                k -= steps
            else:
                # 在这棵树上
                cur *= 10
                k -= 1
        
        return cur
    

class Solution:
    # 原始版本
    def getSteps(self, cur: int, n: int) -> int:
        steps, first, last = 0, cur, cur
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps = self.getSteps(cur, n)
            if steps <= k:
                k-= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

class Solution:
    # 灵神解释版本
    def findKthNumber(self, n: int, k: int) -> int:
        # 逐层统计 node 子树大小
        def count_subtree_size(node: int) -> int:
            size = 0
            left, right = node, node + 1
            while left <= n:
                # 这一层的最小值是 left，最大值是 min(right, n + 1) - 1
                size += min(right, n + 1) - left
                left *= 10  # 继续，计算下一层
                right *= 10
            return size

        node = 1
        k -= 1  # 访问节点 node
        while k > 0:
            size = count_subtree_size(node)
            if size <= k:  # 向右，跳过 node 子树
                node += 1  # 访问 node 右侧兄弟节点
                k -= size  # 访问子树中的每个节点，以及新的 node 节点
            else:  # 向下，深入 node 子树
                node *= 10  # 访问 node 的第一个儿子
                k -= 1  # 访问新的 node 节点
        return node