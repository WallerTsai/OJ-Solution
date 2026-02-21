from bisect import bisect_left, bisect_right
from collections import Counter
from math import inf


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        MN = min(cnt.values())
        ans = 0
        for i in cnt.values():
            if i > MN + k:
                ans += i - MN - k
        return ans  # 错误 存在一种情况是可以把一个元素全部删掉
    

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = inf
        for i in cnt.values():
            temp = 0
            for j in cnt.values():
                if j < i:
                    temp += j
                elif j > i + k:
                    temp += j - i - k
            ans = min(temp, ans)
        return ans  # 63ms O(n ** 2)

class Solution:
    # 记录前缀和
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        cnt = Counter(cnt.values())
        ans = inf
        li = sorted(cnt.keys())
        n = len(li)
        pre_sum = 0
        for i, a in enumerate(li):
            if pre_sum >= ans:
                break
            temp = 0
            for j in range(i + 1, n):
                if li[j] > a + k:
                    temp += (li[j] - a - k) * cnt[li[j]]
            ans = min(temp + pre_sum, ans)
            pre_sum += li[i] * cnt[li[i]]

        return ans  # 63ms

class Solution:
    # 前缀和加上二分查找
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        cnt = Counter(cnt.values())
        ans = inf
        li = sorted(cnt.keys())
        n = len(li)
        pre_sum = 0
        for i in li:
            if pre_sum >= ans:
                break
            temp = 0
            j = bisect_right(li, i + k)
            for a in range(j,n):
                temp += (li[a] - i - k) * cnt[li[a]]
            ans = min(temp + pre_sum, ans)
            pre_sum += i * cnt[i]

        return ans  # 55ms

class Solution:
    # 滑动窗口
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = sorted(Counter(word).values())
        max_save = s = right = 0
        for base in cnt:
            mx = base + k
            while right < len(cnt) and cnt[right] <= mx:
                s += cnt[right]
                right += 1
            # 现在 s 表示出现次数不变的字母个数之和
            # 再加上出现次数减少为 mx 的 len(cnt)-right 种字母，即为保留的字母总数
            max_save = max(max_save, s + mx * (len(cnt) - right))
            # 下一轮循环 base 全删
            s -= base
        return len(word) - max_save # 55ms

fun = Solution()
fun.minimumDeletions("aabcaba",0)