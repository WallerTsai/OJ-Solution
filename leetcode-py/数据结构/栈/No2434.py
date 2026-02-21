
class Solution:
    def robotWithString(self, s: str) -> str:

        n = len(s)
        sub_min = [27] * n
        sub_i = n
        sub_n = 27
        for i in range(n - 1, -1, -1):
            j = ord(s[i]) - ord('a') + 1
            if j <= sub_n:
                sub_i = i
                sub_n = j
            sub_min[i] = sub_i

        ans = ""
        pre = 0
        for i, num in enumerate(sub_min):
            if i + 1 < n and num != sub_min[i + 1]:
                ans += s[pre : i+ 1][::-1]
                pre = i + 1
            elif i + 1 == n:
                ans += s[pre:][::-1]

        return ans  # 错误 # 想复杂了
    

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        suf_min = ["z"] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], s[i])
        
        ans = []
        st = []
        for i, ch in enumerate(s):
            st.append(ch)
            while st and st[-1] <= suf_min[i + 1]:
                ans.append(st.pop())
        return "".join(ans)


fun = Solution()
fun.robotWithString("caba")
l = [1,2,3,4]
print(l[2:-1:-1])