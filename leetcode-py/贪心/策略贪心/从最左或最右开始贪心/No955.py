from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        is_vaild = False
        ans = 0
        for li in zip(*strs):
            print(li)
            for a, b in pairwise(li):
                if b < a:
                    ans += 1
                    is_vaild = False
                    break
                elif b > a:
                    is_vaild = True
            if is_vaild:
                break
        return ans  # 错误 ["xga","xfb","yfa"]
    

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        q = deque()
        aset = set()
        n = len(strs)
        m = len(strs[0])
        q.append([0, n, 0])
        while q:
            l, r, i = q.popleft()

            if i == m:
                continue

            pre = '0'
            temp_li = []
            is_vaild = True
            cur_l = l
            while cur_l < r:
                ch = strs[cur_l][i]
                if ch < pre:
                    aset.add(i)
                    is_vaild = False
                    break
                elif ch > pre:
                    pre = ch
                else:
                    pre_l = cur_l - 1
                    while cur_l + 1 < r and strs[cur_l + 1][i] == pre:
                        cur_l += 1
                    temp_li.append([pre_l, cur_l + 1, i + 1])
                cur_l += 1
            if is_vaild:
                q.extend(temp_li)
            else:
                q.append([l, r, i + 1])
        return len(aset)    # 错误
    

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        is_vaild = False
        aset = set()
        li_same = [[0, len(strs)]]
        for i, li in enumerate(zip(*strs)):
            # 先检查一遍有效不
            is_vaild = True
            for a, b in pairwise(li):
                if b < a:
                    aset.add(i)
                    is_vaild = False
                    break
            if not is_vaild:
                continue

            # 有效后检查上一组相同情况
            nx_li_same = []
            for l, r in li_same:
                ptr = l
                while ptr < r:
                    ch = li[ptr]
                    nx_ptr = ptr + 1
                    if nx_ptr < r and li[nx_ptr] == ch:
                        while nx_ptr < r and li[nx_ptr] == ch:
                            nx_ptr += 1
                        nx_li_same.append([ptr, nx_ptr])
                    ptr = nx_ptr
            if not nx_li_same:
                break
            li_same = nx_li_same

        return len(aset)    # 错误

                        
class Solution:
    # 这份代码是请求 AI 修理我的第二份代码bug而得到的
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # 初始状态：所有的行 [0, n] 都是“纠缠”在一起的，没有区分开
        # 相当于你代码中 q.append([0, n])，但我们不需要存列索引 i，因为外层循环控制列
        groups = [[0, n]] 
        deletion_count = 0
        
        # 按列顺序遍历 (相当于你代码中的 i)
        for i in range(m):
            is_valid_col = True
            
            # 1. 检查当前列 i 对于所有现存的 groups 是否合法
            for l, r in groups:
                # 遍历这个区间内的行
                for k in range(l, r - 1):
                    # 如果出现降序，说明这一列必须删掉
                    if strs[k][i] > strs[k+1][i]:
                        is_valid_col = False
                        break
                if not is_valid_col:
                    break
            
            # 2. 根据检查结果做决定
            if not is_valid_col:
                # 如果这一列在任何一个 group 里导致了乱序，这列必须全局删除
                deletion_count += 1
                # groups 不需要变，因为这一列被忽略了，行之间的“纠缠”关系没变
            else:
                # 如果这一列合法，它可能会打破某些 tie (平局)，我们需要更新 groups
                next_groups = []
                for l, r in groups:
                    # 在当前区间 [l, r] 内寻找新的子区间
                    cur_start = l
                    for k in range(l, r - 1):
                        # 如果当前行比下一行小，说明它们在这里分出胜负了，断开连接
                        if strs[k][i] < strs[k+1][i]:
                            # 将刚才累积的相等部分存入 next_groups
                            if k + 1 - cur_start > 1:
                                next_groups.append([cur_start, k + 1])
                            cur_start = k + 1 # 新的起点
                    
                    # 处理该 group 的收尾部分
                    if r - cur_start > 1:
                        next_groups.append([cur_start, r])
                
                groups = next_groups
                
        return deletion_count   # 双 100%


class Solution:
    # 这份代码是请求 AI 修理我的第二份代码bug而得到的
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        groups = [[0, n]] 
        ans = 0
        
        for i in range(m):
            is_valid_col = True
            
            # 检查当前列 i 对于所有现存的 groups 是否合法
            for l, r in groups:
                for k in range(l, r - 1):
                    if strs[k][i] > strs[k+1][i]:
                        is_valid_col = False
                        break
                if not is_valid_col:
                    break
            
            if not is_valid_col:
                # 这列必须全局删除
                ans += 1
                continue
            
            next_groups = []
            for l, r in groups:
                # 在当前区间 [l, r] 内寻找新的子区间
                cur_start = l
                for k in range(l, r - 1):
                    if strs[k][i] < strs[k+1][i]:
                        # 出现断开
                        # 只有当切下来的这一段长度大于1（说明里面是相等的），才需要保留到下一轮
                        if k > cur_start:
                            next_groups.append([cur_start, k + 1])
                        cur_start = k + 1
                # 处理该 group 的收尾部分
                if r - cur_start > 1:
                    next_groups.append([cur_start, r])
        
            groups = next_groups
                
        return ans  # 0ms
    

class Solution:
    # 灵神
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        a = [''] * n  # 最终得到的字符串数组
        ans = 0
        for j in range(m):
            for i in range(n - 1):
                if a[i] + strs[i][j] > a[i + 1] + strs[i + 1][j]:
                    # j 列不是升序，必须删
                    ans += 1
                    break
            else:
                # j 列是升序，不删更好
                for i, s in enumerate(strs):
                    a[i] += s[j]
        return ans  # 11ms


class Solution:
    # 灵神
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        check_list = list(range(n - 1))

        ans = 0
        for j in range(m):
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    # j 列不是升序，必须删
                    ans += 1
                    break
            else:
                # j 列是升序，不删更好
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        # 相邻字母相等，下一列 i 和 i+1 需要继续比大小
                        check_list[new_size] = i  # 原地覆盖
                        new_size += 1
                del check_list[new_size:]
        return ans  # 双100%
    

fun = Solution()
fun.minDeletionSize(["xc","yb","za"])



