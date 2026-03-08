from sortedcontainers import SortedList # type: ignore

class Solution:
    # 灵神
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        not_vis = [SortedList(range(0, n + 1, 2)), SortedList(range(1, n + 1, 2))]
        not_vis[0].add(n + 1)  # 哨兵，下面 sl[idx] <= mx 无需判断越界
        not_vis[1].add(n + 1)

        start = s.count('0')  # 起点
        not_vis[start % 2].discard(start)
        q = [start]
        ans = 0
        while q:
            tmp = q
            q = []
            for z in tmp:
                if z == 0:  # 没有 0，翻转完毕
                    return ans
                # not_vis[mn % 2] 中的从 mn 到 mx 都可以从 z 翻转到
                mn = z + k - 2 * min(k, z)
                mx = z + k - 2 * max(0, k - n + z)
                sl = not_vis[mn % 2]
                idx = sl.bisect_left(mn)
                while sl[idx] <= mx:
                    j = sl.pop(idx)  # 注意 pop(idx) 会使后续元素向左移，不需要写 idx += 1
                    q.append(j)
            ans += 1
        return -1