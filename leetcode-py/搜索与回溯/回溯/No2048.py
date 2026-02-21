from bisect import bisect_right

# leetcode 大佬
# 预处理所有数值平衡数
Balanced_Num = []
n = 7
cnt = [0] * n
def dfs(i, x):
    if i == n:
        if x == 0:
            return
        for j in range(1, 7):
            if cnt[j] > 0 and cnt[j] != j:
                return
        Balanced_Num.append(x)
        return
    
    low = 0 if x == 0 else 1
    for k in range(low, 7):
        if k == 0 or cnt[k] < k:
            cnt[k] += 1
            dfs(i+1, 10*x + k)
            cnt[k] -= 1
dfs(0, 0)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        j = bisect_right(Balanced_Num, n)
        return Balanced_Num[j]