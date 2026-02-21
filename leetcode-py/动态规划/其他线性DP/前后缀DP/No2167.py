class Solution:
    # 灵神
    def minimumTime(self, s: str) -> int:
        n = len(s)
        suf_list = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                suf_list[i] = suf_list[i + 1]
            else:
                suf_list[i] = min(suf_list[i + 1] + 2, n - i)
        
        ans = suf_list[0]
        pre = 0
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
                ans = min(ans, pre + suf_list[i + 1])
        
        return ans
    

class Solution:
    # 灵神
    def minimumTime(self, s: str) -> int:
        ans = n = len(s)
        pre = 0
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
            ans = min(ans, pre + n - 1 - i)
        return ans
    

class Solution:
    # 前后缀分解
    def minimumTime(self, s: str) -> int:
        n = len(s)
        pre = [0] * (n + 1)
        suf = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == '0':
                pre[i + 1] = pre[i]
            else:
                pre[i + 1] = min(pre[i] + 2, i + 1)
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == '0':
                suf[i] = suf[i + 1]
            else:
                suf[i] = min(suf[i + 1] + 2, n - i)
        # pre[i] 不包含 i
        # suf[i] 包含   i
        ans = n
        for i in range(n + 1):
            ans = min(ans, pre[i] + suf[i])
        return ans  # 1111ms



# gemini 代码
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        ans = n  # 最差情况：全删
        
        # 记录当前省下的最多的钱
        max_save = 0
        current_save = 0
        
        for char in s:
            if char == '0':
                current_save += 1  # 遇到 0 可以省 1 块钱
            else:
                current_save -= 1  # 遇到 1 单点删要多花 1 块钱
                
            # Kadane 核心逻辑：如果省的钱变成负数了，说明这段策略亏本，重新开始攒钱
            if current_save < 0:
                current_save = 0
                
            # 更新历史上省钱最多的一段
            if current_save > max_save:
                max_save = current_save
                
        return n - max_save
    

class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)

        # 1. 两端连续清除的代价: n - (j - i + 1)
        # 2. 中间单点清除的代价: 2 * count1(i, j)
        # 其中: (j - i + 1) = count0(i, j) + count1(i, j)

        # total = n - (count0(i, j) + count1(i, j)) + 2 * count1(i, j)
        # total = n - (count0(i, j) - count1(i, j))
        # 最小total -> 最大 (count0(i, j) - count1(i, j))
        
        count = cur = 0
        for ch in s:
            if ch == '0':
                cur += 1
            else:
                cur -= 1
            
            if cur < 0: # 直接抛弃这一段
                cur = 0

            count = max(count, cur)
        
        return n - count
