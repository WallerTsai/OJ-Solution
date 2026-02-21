from collections import Counter, deque
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        changed.sort()
        aset = set(changed)
        ans = []
        for num in changed:
            if num not in aset:
                continue
            x = 2 * num 
            if x not in aset:
                return []
            aset.discard(x)
            ans.append(num)
        return ans  # 错误，有重复元素


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        changed.sort()
        cnt = Counter(changed)
        ans = []
        for num in changed:
            if num not in cnt:
                continue
            x = 2 * num 
            if x not in cnt:
                return []
            cnt[num] -= 1
            if cnt[num] == 0:
                cnt.pop(num)
            cnt[x] -= 1
            if cnt[x] == 0:
                cnt.pop(x)
            ans.append(num)
        return ans  # 251ms
    

class Solution:
    # 灵神
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        q = deque()
        for x in changed:
            if q:
                if q[0] < x:
                    return []
                if q[0] == x:
                    q.popleft()
                    continue
            ans.append(x)
            q.append(2 * x)
        return [] if q else ans # 135ms


class Solution:
    # 灵神
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        # 单独处理 0
        cnt0 = cnt.pop(0, 0)
        if cnt0 % 2:
            return []
        ans = [0] * (cnt0 // 2)

        for x in cnt:
            # 如果 x/2 在 cnt 中，则跳过
            if x % 2 == 0 and x // 2 in cnt:
                continue
            # 把 x, 2x, 4x, 8x, ... 全部配对
            while x in cnt:
                # 每次循环，把 cnt_x 个 x 和 cnt_x 个 2x 配对
                cnt_x = cnt[x]
                # 无法配对，至少要有 cnt_x 个 2x
                if cnt_x > cnt[x * 2]:
                    return []
                ans.extend([x] * cnt_x)
                if cnt_x < cnt[x * 2]:
                    # 还剩下一些 2x
                    cnt[x * 2] -= cnt_x
                    x *= 2
                else:
                    x *= 4
        return ans  # 107ms