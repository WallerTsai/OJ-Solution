import bisect
from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        if n * (n + 1) // 2 < k:
            return -1

        star = [0] * n  # 避免在二分内部反复创建/初始化列表

        def check(m: int) -> bool:
            m += 1
            for j in range(m):
                star[order[j]] = m
            cnt = 0
            last = -1  # 上一个 '*' 的位置
            for i, x in enumerate(star):
                if x == m:  # s[i] 是 '*'
                    last = i
                cnt += last + 1
                if cnt >= k:  # 提前退出循环
                    return True
            return False

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right    # 1011ms
    
class Solution:
    # 双端链表  + 逆向思维
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        cnt = n * (n + 1) // 2
        if cnt < k:  # 全改成星号也无法满足要求
            return -1

        # 数组模拟双向链表
        pre = list(range(-1, n))
        nxt = list(range(1, n + 2))

        for t in range(n - 1, -1, -1):
            i = order[t]
            l, r = pre[i], nxt[i]
            cnt -= (i - l) * (r - i)
            if cnt < k:
                return t
            # 删除链表中的 i
            nxt[l] = r
            pre[r] = l  # 182ms

class Solution:
    # 区间维护
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n*(n+1)//2
        # 干净子串总和
        clean_sum = total
        # 比较临界值
        fx = total - k
        # 初始就是一个大的、完整的干净子串
        starts = [0]
        ends = [n-1]

        def get_clean_num(l,r):
            len = r-l+1
            return len*(len+1)//2

        # 在哪个位置返回，就是答案
        for ans,p in enumerate(order):
            # 先找一下这个p在目前维护的区间段里哪个位置
            i = bisect.bisect_right(starts,p) - 1
            l = starts[i]
            r = ends[i]
            # 弹出对应的子串
            starts.pop(i)
            ends.pop(i)
            # 更新当前干净子串总和
            clean_sum -= get_clean_num(l,r)

            # 加入子串，要注意插入位置刚好是首/尾的情况
            if(p == l):
                starts.insert(i,p+1)
                ends.insert(i,r)
                clean_sum += get_clean_num(l+1, r)
                # print("左边")
            elif(p == r):
                starts.insert(i,l)
                ends.insert(i, p-1)
                clean_sum += get_clean_num(l , r-1)
                # print("右边")
            # 插2段
            else:
                # print("中间")
                starts.insert(i,l)
                ends.insert(i,p-1)
                clean_sum += get_clean_num(l, p-1)
                # 插第2段，要往后移动一下
                starts.insert(i+1, p+1)
                ends.insert(i+1, r)
                clean_sum += get_clean_num(p+1, r)

            # print(clean_sum)
            # print("维护段 ",starts,ends)
            if(clean_sum <= fx):
                return ans
        
        return -1
    
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        count=0
        n=len(s)
        tmp=[-1,n]
        if (n+1)*n//2<k:
            return -1
        for i in range(n):
            l=0
            r=i+2
            o=order[i]
            while l<r-1:
                mid=(l+r)//2
                if tmp[mid]>o:
                    r=mid
                else:
                    l=mid
            count+=(o-tmp[l])*(tmp[l+1]-o)
            if count>=k:
                break
            tmp.insert(l+1,o)
        return i