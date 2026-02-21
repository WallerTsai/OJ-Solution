class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pos0 = [i for i in range(n) if s[i] == "0"]
        total1 = n - len(pos0)
        pos0.append(n)
        ans = 0
        p0 = 0
        for i in range(n):
            if s[i] == "1":
                ans += pos0[p0] - i
            for j in range(p0, len(pos0) - 1):
                cnt0 = j - p0 + 1  # #0 in [i, pos0[j]]
                if cnt0 * cnt0 > total1:
                    break
                cnt1 = pos0[j] - i + 1 - cnt0  # #1 in [i, pos0[j]]
                extra1 = pos0[j + 1] - pos0[j] - 1
                if cnt0 * cnt0 <= cnt1:
                    ans += extra1 + 1
                elif cnt0 * cnt0 <= cnt1 + extra1:
                    ans += cnt1 + extra1 - cnt0 * cnt0 + 1
            if s[i] == "0":
                p0 += 1
        return ans



# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    # 灵神
    def numberOfSubstrings(self, s: str) -> int:
        pos0 = [-1]  # 哨兵，方便处理 cnt0 达到最大时的计数
        total1 = 0  # [0,r] 中的 1 的个数
        ans = 0

        for r, ch in enumerate(s):
            if ch == '0':
                pos0.append(r)  # 记录 0 的下标
            else:
                total1 += 1
                ans += r - pos0[-1]  # 单独计算不含 0 的子串个数

            # 倒着遍历 pos0，就相当于在从小到大枚举 cnt0
            for i in range(len(pos0) - 1, 0, -1):
                cnt0 = len(pos0) - i
                if cnt0 * cnt0 > total1:
                    break
                p, q = pos0[i - 1], pos0[i]
                cnt1 = r - q + 1 - cnt0  # [q,r] 中的 1 的个数 = [q,r] 的长度 - cnt0
                ans += max(q - max(cnt0 * cnt0 - cnt1, 0) - p, 0)

        return ans