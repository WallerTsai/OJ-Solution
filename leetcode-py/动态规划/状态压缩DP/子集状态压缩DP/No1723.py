from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)

        def check(limit):
            m = count = 0
            for x in jobs:
                if count + x <= limit:
                    count += x
                else:
                    m += 1
                    count = x
            if count:
                m += 1
            return m <= k
        
        left, right = jobs[0], sum(jobs[:k])
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left # 错误  在 check 里面不能贪心



class Solution:
    # +No698
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)

        def check(limit):
            workors = [0] * k

            def backtrack(idx):
                if idx == n:
                    return True
                
                cur = jobs[idx]
                for i in range(k):
                    if i and workors[i] == workors[i - 1]:
                        continue
                    workors[i] += cur
                    if workors[i] <= limit and backtrack(idx + 1):
                        return True
                    workors[i] -= cur

                return False
            
            return backtrack(0)
        
        left, right = jobs[0], sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left # 8ms
    
# 灵神
subsets = [[] for _ in range(1 << 12)]
for i in range(1 << 12):
    s = i
    while s:
        subsets[i].append(s)
        s = (s - 1) & i

class Solution:
    def minimumTimeRequired(self, cookies: List[int], k: int) -> int:
        m = 1 << len(cookies)
        SUM = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                SUM[bit | j] = SUM[j] + v

        f = SUM.copy()
        for _ in range(1, k):
            for j in range(m - 1, 0, -1):
                for s in subsets[j]:
                    v = f[j ^ s]
                    if SUM[s] > v: v = SUM[s]  # 不要用 max 和 min，那样会有额外的函数调用开销
                    if v < f[j]: f[j] = v
        return f[-1]
