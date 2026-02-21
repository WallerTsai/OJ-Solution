class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        index2 = index3 = index5 = 0
        for i in range(1,n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]:
                index2 += 1
            if dp[i] == 3 * dp[index3]:
                index3 += 1
            if dp[i] == 5 * dp[index5]:
                index5 += 1
        return dp[-1]
    
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = curr_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly
