from bisect import bisect_left,bisect_right
from collections import defaultdict
import string



class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        tran_list = [0] * n
        last_index = [-1] * 26
        # 初始处理
        for i,c in enumerate(s):
            order = ord(c) - 97
            if last_index[order] != -1:
                if tran_list[last_index[order]] == 0:
                    tran_list[last_index[order]] = -1
                elif tran_list[last_index[order]] == 1:
                    tran_list[last_index[order]] = -2
                tran_list[i] = 1
            else:
                tran_list[i] = 0
            last_index[order] = i

        ans1 = ans2 = count = 0
        for x in tran_list:
            if x == -2:
                continue
            count += x
            if x == 0:
                ans2 += 1
            if count == 0:
                ans1 += 1
                ans2 = 0
            if ans1 + ans2 >= k:
                return True
        return False # 一个思路不对，最后几个示例给制裁，主要是忽略了包含关系
    
class Solution:
    # 跟着leetcode大佬
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # 先预处理每个字母的最左最右下标
        lpos = {}
        rpos = {}
        for i,c in enumerate(s):
            rpos[c] = i
            if c not in lpos:
                lpos[c] = i
        
        # 枚举每个字母 + 哈希表
        n = len(s)
        area = []
        dt = set() # 用于给area去重
        # 开始枚举每个字母
        for c in string.ascii_lowercase:
            if c not in lpos:
                continue
            l,r = lpos[c],rpos[c]
            for i in range(lpos[c],rpos[c] + 1):
                _c = s[i]
                x,y = lpos[_c],rpos[_c]
                if x < l:
                    c = x
                if y > r:
                    r = y
            if (l,r) != (0,n-1):
                if (l,r) in dt:
                    continue
                area.append((l,r))
                dt.add((l,r))

        ans = 0
        # 需要保证area中不重叠,且是最小区间
        m = len(area)
        for i in range(m):
            l,r = area[i]
            # for j in range(i+1,m):
            # 应该是下面这个
            for j in range(m):
                x,y = area[j]
                # 同一个
                if i == j:
                    continue
                # 没有交集
                if x > r or y < l:
                    continue

                # 被包含于
                if x < l and r < y:
                    continue

                # 部分相交和包含小的
                break
            else:
                ans += 1
        
        return ans >= k # 还是过不了,照抄抄错可能

class Solution:
    # 跟着leetcode大佬
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # 先预处理每个字母的最左最右下标
        lpos = {}
        rpos = {}
        for i,c in enumerate(s):
            rpos[c] = i
            if c not in lpos:
                lpos[c] = i
        
        # 枚举每个字母 + 哈希表
        n = len(s)
        area = []
        dt = set() # 用于给area去重
        # 开始枚举每个字母
        for c in string.ascii_lowercase:
            if c not in lpos:
                continue
            l,r = lpos[c],rpos[c]
            for i in range(lpos[c],rpos[c] + 1):
                _c = s[i]
                x,y = lpos[_c],rpos[_c]
                # 扩展范围
                if x < l:
                    l = x
                if y > r:
                    r = y
            if (l,r) != (0,n-1):
                if (l,r) in dt:
                    continue
                area.append((l,r))
                dt.add((l,r))

        ans = 0
        # 需要保证area中不重叠,且是最小区间
        for i,(l,r) in enumerate(area):
            for j,(x,y) in enumerate(area):
                # 同一个
                if i == j:
                    continue
                # 没有交集
                if x > r or y < l:
                    continue

                # 被包含于
                if x < l and r < y:
                    continue

                # 部分相交和包含小的
                break
            else:
                ans += 1
        return ans >= k # 954ms

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        pos = [[] for _ in range(26)]
        for idx, c in enumerate(s):
            pos[ord(c) - ord('a')].append(idx)
        
        vec = []
        for i in range(26):
            if not pos[i]:
                continue
            l = pos[i][0]
            r = pos[i][-1]
            flag = True
            while flag:
                flag = False
                for j in range(26):
                    if not pos[j]:
                        continue
                    left = bisect_left(pos[j], l)
                    right_idx = bisect_right(pos[j], r)
                    cnt = right_idx - left
                    if cnt > 0 and cnt < len(pos[j]):
                        new_l = min(l, pos[j][0])
                        new_r = max(r, pos[j][-1])
                        if new_l != l or new_r != r:
                            l, r = new_l, new_r
                            flag = True
            if l > 0 or r < n - 1:
                vec.append((r, l))
        
        vec.sort()
        R = -1
        cnt = 0
        for p in vec:
            curr_l = p[1]
            if curr_l > R:
                R = p[0]
                cnt += 1
                if cnt >= k:
                    return True
        return cnt >= k # 175ms


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        pos = defaultdict(list)
        for idx, c in enumerate(s):
            pos[c].append(idx)
        
        vec = []
        pos_keys = pos.keys()
        for i in pos_keys:
            l = pos[i][0]
            r = pos[i][-1]
            flag = True
            while flag:
                # 我们以包含了 a 的特殊子串为例。假设 a 最左边出现在下标 la，最右边出现在下标 ra，
                # 那么为了让子串最短，一开始我们就先尝试子串 s[la:ra]。如果这个子串里没有别的字母，就万事大吉；
                # 但如果出现了其它字母，比如又出现了 b 和 c，那这个子串就得包含所有的 b 和 c，
                # 重新检查这个子串，如果子串里确实只有 abc，就万事大吉；但如果出现了其它字母，那我们又得用这些字母更新子串的范围...
                flag = False
                for j in pos_keys:
                    left_idx = bisect_left(pos[j], l)
                    right_idx = bisect_right(pos[j], r)
                    cnt = right_idx - left_idx
                    if cnt > 0 and cnt < len(pos[j]):
                        # 如果是 区间i 包含 区间j 或者 没有交集则跳过
                        # 否则更新区间
                        l = min(l, pos[j][0])
                        r = max(r, pos[j][-1])
                        flag = True
            if l > 0 or r < n - 1:
                vec.append((r, l))
        
        # leetcode 435
        vec.sort()
        pre_r = -1
        cnt = 0
        for p in vec:
            curr_l = p[1]
            if curr_l > pre_r:
                pre_r = p[0]
                cnt += 1
        return cnt >= k # 119ms