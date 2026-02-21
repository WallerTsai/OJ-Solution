from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class Solution:
    # 灵神 
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = defaultdict(int)
        L, R = SortedList(), SortedList()
        sum_l = 0

        def add(val: int):
            if cnt[val] == 0:
                return 
            p = (cnt[val], val)
            if L and p > L[0]:
                nonlocal sum_l
                sum_l += p[0] * p[1]
                L.add(p)
            else:
                R.add(p)

        def remove(val: int):
            if cnt[val] == 0:
                return
            p = (cnt[val], val)
            if p in L:
                nonlocal sum_l
                sum_l -= p[0] * p[1]
                L.remove(p)
            else:
                R.remove(p)

        def l2r():
            nonlocal sum_l
            p = L[0]
            sum_l -= p[0] * p[1]
            L.remove(p)
            R.add(p)

        def r2l():
            nonlocal sum_l
            p = R[-1]
            sum_l += p[0] * p[1]
            R.remove(p)
            L.add(p)


        ans = [0] * (len(nums) - k + 1)
        for r, in_ in enumerate(nums):
            # 添加 in_
            remove(in_)
            cnt[in_] += 1
            add(in_)

            l = r - k + 1
            if l < 0:
                continue

            # 维护大小
            while R and len(L) < x:
                r2l()
            while len(L) > x:
                l2r()
            ans[l] = sum_l

            # 移除 out
            out = nums[l]
            remove(out)
            cnt[out] -= 1
            add(out)

        return ans  # 3765ms






import heapq
from typing import List

class Solution:
    # leetcode 最快
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k == 0: return []
        if x == 0:  # 取前0个 → 和为0
            return [0]*(n-k+1)

        # 1) 首窗初始化
        freq = {}
        win_sum = 0
        for i in range(k):
            v = nums[i]
            win_sum += v
            freq[v] = freq.get(v, 0) + 1

        # 选出前x：容量为x的最小堆，键=(cnt,val)
        top_heap = []
        for v, f in freq.items():
            heapq.heappush(top_heap, (f, v))
            if len(top_heap) > x:
                heapq.heappop(top_heap)

        in_top = {v for f, v in top_heap}
        top_sum = sum(v * freq[v] for v in in_top)

        # 其余进候补最大堆（键=(-cnt,-val)）
        rest_heap = []
        for v in freq:
            if v not in in_top:
                heapq.heappush(rest_heap, (-freq[v], -v))

        # ——— 实用小工具：懒删除清理堆顶 ———
        def prune_top():
            while top_heap:
                f, v = top_heap[0]
                if (v not in in_top) or (freq.get(v, 0) != f):
                    heapq.heappop(top_heap)
                else:
                    break

        def prune_rest():
            while rest_heap:
                nf, nv = rest_heap[0]
                f, v = -nf, -nv
                if (v in in_top) or (freq.get(v, 0) != f):
                    heapq.heappop(rest_heap)
                else:
                    break

        # ——— 重平衡：人数=need，必要时边界交换 ———
        def rebalance():
            nonlocal top_sum
            U = len(freq)
            need = min(x, U)

            prune_top(); prune_rest()

            # 补足
            while len(in_top) < need and rest_heap:
                nf, nv = heapq.heappop(rest_heap)
                f, v = -nf, -nv
                if (v in in_top) or (freq.get(v, 0) != f):  # 旧快照
                    continue
                in_top.add(v)
                top_sum += v * f
                heapq.heappush(top_heap, (f, v))
                prune_rest()

            # 裁剪
            while len(in_top) > need:
                prune_top()
                if not top_heap: break
                f, v = heapq.heappop(top_heap)
                if (v not in in_top) or (freq.get(v, 0) != f):
                    continue
                in_top.remove(v)
                top_sum -= v * f
                heapq.heappush(rest_heap, (-f, -v))

            # 边界交换（尽量一次拉直；可循环几次，通常一次足够）
            while True:
                prune_top(); prune_rest()
                if not top_heap or not rest_heap: break
                f_top, v_top = top_heap[0]
                f_res, v_res = -rest_heap[0][0], -rest_heap[0][1]
                if (f_res, v_res) > (f_top, v_top):
                    heapq.heappop(top_heap); heapq.heappop(rest_heap)
                    # 再次校验有效性
                    if freq.get(v_top, 0) != f_top or freq.get(v_res, 0) != f_res:
                        # 旧快照，压回新快照后继续
                        if v_top in in_top:
                            heapq.heappush(top_heap, (freq.get(v_top, 0), v_top))
                        if v_res not in in_top:
                            heapq.heappush(rest_heap, (-freq.get(v_res, 0), -v_res))
                        continue
                    # 交换成员
                    in_top.remove(v_top); in_top.add(v_res)
                    top_sum -= v_top * f_top
                    top_sum += v_res * f_res
                    heapq.heappush(rest_heap, (-f_top, -v_top))
                    heapq.heappush(top_heap, (f_res, v_res))
                else:
                    break

        # 记录首窗答案
        ans = []
        ans.append(win_sum if len(freq) < x else top_sum)

        # 2) 滑动窗口
        left = 0
        for right in range(k, n):
            # 移出左端
            old = nums[left]; left += 1
            win_sum -= old
            oldf = freq.get(old, 0)
            if oldf:
                newf = oldf - 1
                if old in in_top:
                    top_sum -= old  # 频次-1 → 对 top_sum 的差分
                if newf == 0:
                    del freq[old]
                    if old in in_top:
                        in_top.remove(old)
                else:
                    freq[old] = newf
                    # 懒快照：按当前归属压回原堆
                    if old in in_top:
                        heapq.heappush(top_heap, (newf, old))
                    else:
                        heapq.heappush(rest_heap, (-newf, -old))

            # 加入右端
            cur = nums[right]
            win_sum += cur
            was = freq.get(cur, 0)
            freq[cur] = was + 1
            if cur in in_top:
                top_sum += cur  # 频次+1 → 对 top_sum 的差分
                heapq.heappush(top_heap, (freq[cur], cur))
            else:
                # 新值或候补，先放 rest；是否提拔交给 rebalance
                heapq.heappush(rest_heap, (-freq[cur], -cur))

            # 整理边界
            rebalance()

            # 输出本窗答案
            ans.append(win_sum if len(freq) < x else top_sum)

        return ans
    


class Solution:
    # 对顶堆
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        pass




